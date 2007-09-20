"""Cobalt component XML-RPC server."""

__revision__ = '$Revision: 758 $'

__all__ = [
    "TCPServer", "XMLRPCRequestHandler", "XMLRPCServer",
    "find_intended_location",
]

import sys
import os
import socket
import SocketServer
import SimpleXMLRPCServer
import base64
import signal
from ConfigParser import SafeConfigParser, NoSectionError, NoOptionError
import urlparse

import tlslite.integration.TLSSocketServerMixIn
import tlslite.api
from tlslite.api import \
    TLSSocketServerMixIn, parsePrivateKey, \
    X509, X509CertChain, SessionCache, TLSError

from Cobalt.Proxy import ComponentProxy


def find_intended_location (component, config_files=None):
    """Determine a component's intended service location.
    
    Arguments:
    component -- component to find records for
    
    Keyword arguments:
    config_files -- list of configuration files to use (default ["/etc/cobalt.conf"])
    """
    if not config_files:
        config_files = ["/etc/cobalt.conf"]
    config = SafeConfigParser()
    config.read(config_files)
    try:
        url = config.get("components", component.name)
    except (NoSectionError, NoOptionError):
        return ("127.0.0.1", 0)
    location = urlparse.urlparse(url)[1]
    if ":" in location:
        host, port = location.split(":")
        port = int(port)
        location = (host, port)
    else:
        location = (location, 0)
    return location


class TLSConnection (tlslite.api.TLSConnection):
    
    """TLSConnection supporting additional socket methods.
    
    Methods:
    shutdown -- shut down the underlying socket
    """
    
    def shutdown (self, *args, **kwargs):
        """Shut down the underlying socket."""
        return self.sock.shutdown(*args, **kwargs)

#monkeypatch TLSSocketServerMixIn's module to use new TLSConnection
tlslite.integration.TLSSocketServerMixIn.TLSConnection = TLSConnection


class TCPServer (TLSSocketServerMixIn, SocketServer.TCPServer, object):
    
    """TCP server supporting SSL encryption.
    
    Methods:
    handshake -- perform a SSL/TLS handshake
    
    Properties:
    url -- A url pointing to this server.
    """
    
    allow_reuse_address = True
    
    def __init__ (self, server_address, RequestHandlerClass, keyfile=None, certfile=None, reqCert=False, timeout=None):
        
        """Initialize the SSL-TCP server.
        
        Arguments:
        server_address -- address to bind to the server
        RequestHandlerClass -- class to handle requests
        
        Keyword arguments:
        keyfile -- private encryption key filename (enables ssl encryption)
        certfile -- certificate file (enables ssl encryption)
        reqCert -- client must present certificate
        timeout -- timeout for non-blocking request handling
        """
        
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)
        
        self.socket.settimeout(timeout)
        
        if keyfile or certfile:
            keyfile = open(keyfile or certfile)
            self.private_key = parsePrivateKey(keyfile.read())
            keyfile.close()
            x509 = X509()
            certfile = open(certfile or keyfile)
            x509.parse(certfile.read())
            certfile.close()
            self.certificate_chain = X509CertChain([x509])
        else:
            if reqCert:
                raise TypeError("use of reqCert requires a keyfile/certfile")
            self.private_key = None
            self.certificate_chain = None
        self.request_certificate = reqCert
        self.sessions = SessionCache()
    
    def handshake (self, connection):
        
        """Perform the SSL/TLS handshake.
        
        Arguments:
        connection -- handshake through this connection
        """
        
        try:
            connection.handshakeServer(
                certChain = self.certificate_chain,
                privateKey = self.private_key,
                reqCert = self.request_certificate,
                sessionCache = self.sessions,
            )
        except TLSError, e:
            return False
        
        connection.ignoreAbruptClose = True
        return True
    
    def finish_request (self, *args, **kwargs):
        """Support optional ssl/tls handshaking."""
        if self.private_key and self.certificate_chain:
            TLSSocketServerMixIn.finish_request(self, *args, **kwargs)
        else:
            SocketServer.TCPServer.finish_request(self, *args, **kwargs)
    
    def _get_secure (self):
        return self.private_key and self.certificate_chain
    secure = property(_get_secure)
    
    def _get_url (self):
        address, port = self.socket.getsockname()
        if self.secure:
            protocol = "https"
        else:
            protocol = "http"
        return "%s://%s:%i" % (protocol, address, port)
    url = property(_get_url)


class XMLRPCRequestHandler (SimpleXMLRPCServer.SimpleXMLRPCRequestHandler):
    
    """Component XML-RPC request handler.
    
    Adds support for HTTP authentication.
    
    Exceptions:
    CouldNotAuthenticate -- client did not present acceptable authentication information
    
    Methods:
    authenticate -- prompt a check of a client's provided username and password
    handle_one_request -- handle a single rpc (optionally authenticating)
    """
    
    class CouldNotAuthenticate (Exception):
        """Client did not present acceptible authentication information."""
    
    require_auth = False
    credentials = None
    
    def authenticate (self):
        """Authenticate the credentials of the latest client."""
        try:
            header = self.headers['Authorization']
        except KeyError:
            print >> file("outfile", "w"), self.headers
            raise self.CouldNotAuthenticate("client did not present credentials")
        auth_type, auth_content = header.split()
        auth_content = base64.standard_b64decode(auth_content)
        try:
            username, password = auth_content.split(":")
        except ValueError:
            username = auth_content
            password = ""
        try:
            valid_password = self.credentials[username]
        except KeyError:
            raise self.CouldNotAuthenticate("unknown user: %s" % username)
        if password != valid_password:
            raise self.CouldNotAuthenticate("invalid password for %s" % username)
    
    def parse_request (self):
        """Extends parse_request.
        
        Optionally check HTTP authentication when parsing."""
        if not SimpleXMLRPCServer.SimpleXMLRPCRequestHandler.parse_request(self):
            return False
        if self.require_auth:
            try:
                self.authenticate()
            except self.CouldNotAuthenticate:
                code = 401
                message, explanation = self.responses[401]
                self.send_error(code, message)
                return False
        return True


class XMLRPCServer (TCPServer, SimpleXMLRPCServer.SimpleXMLRPCDispatcher, object):
    
    """Component XMLRPCServer.
    
    Methods:
    serve_daemon -- serve_forever in a daemonized process
    serve_forever -- handle_one_request until not self.serve
    shutdown -- stop serve_forever (by setting self.serve = False)
    ping -- return all arguments received
    
    RPC methods:
    ping
    
    (additional system.* methods are inherited from base dispatcher)
    
    Properties:
    require_auth -- the request handler is requiring authorization
    credentials -- valid credentials being used for authentication
    """
    
    def __init__ (self, server_address, RequestHandlerClass=None,
                  keyfile=None, certfile=None,
                  timeout=None,
                  logRequests=False,
                  register=True, allow_none=True, encoding=None):
        
        """Initialize the XML-RPC server.
        
        Arguments:
        server_address -- address to bind to the server
        
        Keyword arguments:
        keyfile -- private encryption key filename
        certfile -- certificate file
        requestHandler -- request handler used by TCP server
        logRequests -- log all requests (default False)
        register -- presence should be reported to service-location (default True)
        allow_none -- allow None values in xml-rpc
        encoding -- encoding to use for xml-rpc (default UTF-8)
        """
        
        try:
            SimpleXMLRPCServer.SimpleXMLRPCDispatcher.__init__(self, allow_none, encoding)
        except TypeError:
            SimpleXMLRPCServer.SimpleXMLRPCDispatcher.__init__(self)
            self.allow_none = allow_none
            self.encoding = encoding
        
        if not RequestHandlerClass:
            class RequestHandlerClass (XMLRPCRequestHandler):
                """A subclassed request handler to prevent class-attribute conflicts."""
        
        TCPServer.__init__(self,
            server_address, RequestHandlerClass,
            timeout=timeout, keyfile=keyfile, certfile=certfile)
        self.logRequests = logRequests
        self.serve = False
        self.register = register
        self.register_introspection_functions()
        self.register_function(self.ping)
        
        if self.register:
            ComponentProxy("service-location").register(self.instance.name, self.url)
    
    def server_close (self):
        TCPServer.server_close(self)
        if self.register:
            ComponentProxy("service-location").unregister(self.instance.name)
    
    # support Python 2.5-style marshaled dispatch in Python < 2.5
    if sys.version_info[0] < 2 or (sys.version_info[0] == 2 and sys.version_info[1] < 5):
        def _marshaled_dispatch (self, data, dispatch_method=None):
            __doc__ = SimpleXMLRPCServer.SimpleXMLRPCDispatcher.__doc__
            try:
                params, method = xmlrpclib.loads(data)
                if dispatch_method is not None:
                    response = dispatch_method(method, params)
                else:
                    response = self._dispatch(method, params)
                response = (response,)
                response = xmlrpclib.dumps(response, methodresponse=1,
                    allow_none=self.allow_none, encoding=self.encoding)
            except Fault, fault:
                response = xmlrpclib.dumps(fault,
                    allow_none=self.allow_none, encoding=self.encoding)
            except:
                # report exception back to server
                response = xmlrpclib.dumps(
                    xmlrpclib.Fault(1, "%s:%s" % (sys.exc_type, sys.exc_value)),
                    allow_none=self.allow_none, encoding=self.encoding)
            return response
    
    def _get_require_auth (self):
        return getattr(self.RequestHandlerClass, "require_auth", False)
    def _set_require_auth (self, value):
        self.RequestHandlerClass.require_auth = value
    require_auth = property(_get_require_auth, _set_require_auth)
    
    def _get_credentials (self, dummy={}):
        return getattr(self.RequestHandlerClass, "credentials", dummy)
    def _set_credentials (self, value):
        self.RequestHandlerClass.credentials = value
    credentials = property(_get_credentials, _set_credentials)
    
    def serve_daemon (self, pidfile=None):
        
        """Implement serve_forever inside a daemon.
        
        Arguments:
        pidfile -- file in which to record daemon pid
        """
        
        child_pid = os.fork()
        if child_pid != 0:
            return
        
        os.setsid()
        
        child_pid = os.fork()
        if child_pid != 0:
            os._exit(0)
        
        #redirect_file = open(os.devnull, "w+")
        #os.dup2(redirect_file.fileno(), sys.__stdin__.fileno())
        #os.dup2(redirect_file.fileno(), sys.__stdout__.fileno())
        #os.dup2(redirect_file.fileno(), sys.__stderr__.fileno())
        
        os.chdir(os.sep)
        os.umask(0)
        
        pidfile = open(pidfile or os.devnull, "w")
        print >> pidfile, os.getpid()
        pidfile.close()
        
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)
        
        self.serve = True
        self.serve_forever()
        self.server_close()
        os._exit(0)
    
    def serve_forever (self):
        """Serve single requests until (self.serve == False)."""
        
        while self.serve:
            try:
                self.handle_request()
            except socket.timeout:
                pass
            if self.instance:
                self.instance.do_tasks()
    
    def shutdown (self):
        """Signal that automatic service should stop."""
        self.serve = False
    
    def ping (self, *args):
        """Echo response."""
        return args