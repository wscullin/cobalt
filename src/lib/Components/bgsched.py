#!/usr/bin/env python

'''Super-Simple Scheduler for BG/L'''
__revision__ = '$Revision$'

import logging
import sys
import time
import math
import types
import ConfigParser
try:
    set()
except:
    from sets import Set as set

import Cobalt.Logging, Cobalt.Util
from Cobalt.Data import Data, DataDict, ForeignData, ForeignDataDict
from Cobalt.Components.base import Component, exposed, automatic, query
from Cobalt.Proxy import ComponentProxy
from Cobalt.Exceptions import ReservationError, DataCreationError, ComponentLookupError
import xmlrpclib

import Cobalt.SchedulerPolicies

logger = logging.getLogger("Cobalt.Components.scheduler")

SLOP_TIME = 180
DEFAULT_RESERVATION_POLICY = "default"

class Reservation (Data):
    
    """Cobalt scheduler reservation."""
    
    fields = Data.fields + [
        "tag", "name", "start", "duration", "cycle", "users", "partitions",
        "active", "queue", 
    ]
    
    required = ["name", "start", "duration"]
    
    def __init__ (self, spec):
        Data.__init__(self, spec)
        self.tag = spec.get("tag", "reservation")
        self.cycle = spec.get("cycle")
        self.users = spec.get("users", "")
        self.createdQueue = False
        self.partitions = spec.get("partitions", "")
        self.name = spec['name']
        self.start = spec['start']
        self.queue = spec.get("queue", "R.%s" % self.name)
        self.duration = spec.get("duration")
        
    def _get_active(self):
        return self.is_active()
    
    active = property(_get_active)
    
    def update (self, spec):
        if spec.has_key("users"):
            qm = ComponentProxy("queue-manager")
            try:
                qm.set_queues([{'name':self.queue,}], {'users':spec['users']})
            except ComponentLookupError:
                logger.error("unable to contact queue manager when updating reservation users")
                raise
        # try the above first -- if we can't contact the queue-manager, don't update the users
        Data.update(self, spec)

    
    def overlaps(self, start, duration):
        '''check job overlap with reservations'''
        if start + duration < self.start:
            return False

        if self.cycle and duration >= self.cycle:
            return True

        my_stop = self.start + self.duration
        if self.start <= start < my_stop:
            # Job starts within reservation 
            return True
        elif self.start <= (start + duration) < my_stop:
            # Job ends within reservation 
            return True
        elif start < self.start and (start + duration) >= my_stop:
            # Job starts before and ends after reservation
            return True
        if not self.cycle:
            return False
        
        # 3 cases, front, back and complete coverage of a cycle
        cstart = (start - self.start) % self.cycle
        cend = (start + duration - self.start) % self.cycle
        if cstart < self.duration:
            return True
        if cend < self.duration:
            return True
        if cstart > cend:
            return True
        
        return False

    def job_within_reservation(self, job):
        if not self.is_active():
            return False
        
        if job.queue == self.queue:
            job_end = time.time() + 60 * float(job.walltime) + SLOP_TIME
            if not self.cycle:
                res_end = self.start + self.duration
                if job_end < res_end:
                    return True
                else:
                    return False
            else:
                if 60 * float(job.walltime) + SLOP_TIME > self.duration:
                    return False
                
                relative_start = (time.time() - self.start) % self.cycle
                relative_end = relative_start + 60 * float(job.walltime) + SLOP_TIME
                if relative_end < self.duration:
                    return True
                else:
                    return False
        else:
            return False

    
    def is_active(self, stime=False):
        if not stime:
            stime = time.time()
            
        if stime < self.start:
            return False
        
        if self.cycle:
            now = (stime - self.start) % self.cycle
        else:
            now = stime - self.start    
        if now <= self.duration:
            return True

    def is_over(self):
        # reservations with a cycle time are never "over"
        if self.cycle:
            return False
        
        stime = time.time()
        if (self.start + self.duration) <= stime:
            return True
        else:
            return False
        
        

class ReservationDict (DataDict):
    
    item_cls = Reservation
    key = "name"
    
    def q_add (self, *args, **kwargs):
        qm = ComponentProxy("queue-manager")
        try:
            queues = [spec['name'] for spec in qm.get_queues([{'name':"*"}])]
        except ComponentLookupError:
            logger.error("unable to contact queue manager when adding reservation")
            raise
        
        try:
            reservations = Cobalt.Data.DataDict.q_add(self, *args, **kwargs)
        except KeyError, e:
            raise ReservationError("Error: a reservation named %s already exists" % e)
                
        for reservation in reservations:
            if reservation.queue not in queues:
                try:
                    qm.add_queues([{'tag': "queue", 'name':reservation.queue, 'state':"running",
                                    'users':reservation.users, 'policy':DEFAULT_RESERVATION_POLICY}])
                except Exception, e:
                    logger.error("unable to add reservation queue %s (%s)" % \
                                 (reservation.queue, e))
                else:
                    reservation.createdQueue = True
                    logger.info("added reservation queue %s" % (reservation.queue))
            else:
                try:
                    qm.set_queues([{'name':reservation.queue}],
                                  {'state':"running", 'users':reservation.users})
                except Exception, e:
                    logger.error("unable to update reservation queue %s (%s)" % \
                                 (reservation.queue, e))
                else:
                    logger.info("updated reservation queue %s" % reservation.queue)
    
        return reservations
        
    def q_del (self, *args, **kwargs):
        reservations = Cobalt.Data.DataDict.q_del(self, *args, **kwargs)
        qm = ComponentProxy('queue-manager')
        queues = [spec['name'] for spec in qm.get_queues([{'name':"*"}])]
        spec = [{'name': reservation.queue} for reservation in reservations \
                if reservation.createdQueue and reservation.queue in queues and \
                not self.q_get([{'queue':reservation.queue}])]
        try:
            qm.set_queues(spec, {'state':"dead"})
        except Exception, e:
            logger.error("problem disabling reservation queue (%s)" % e)
        return reservations


                

class Job (ForeignData):
    
    """A cobalt job."""
    
    fields = ForeignData.fields + [
        "nodes", "location", "jobid", "state", "index", "walltime", "queue", "user", "submittime", 
        "system_state", "starttime", "project",
    ]
    
    def __init__ (self, spec):
        ForeignData.__init__(self, spec)
        spec = spec.copy()
        self.partition = "none"
        self.nodes = spec.pop("nodes", None)
        self.location = spec.pop("location", None)
        self.jobid = spec.pop("jobid", None)
        self.state = spec.pop("state", None)
        self.index = spec.pop("index", None)
        self.walltime = spec.pop("walltime", None)
        self.queue = spec.pop("queue", None)
        self.user = spec.pop("user", None)
        self.submittime = spec.pop("submittime", None)
        self.system_state = spec.pop("system_state", None)
        self.starttime = spec.pop("starttime", None)
        self.project = spec.pop("project", None)
        
        logger.info("Job %s/%s: Found job" % (self.jobid, self.user))

class JobDict(ForeignDataDict):
    item_cls = Job
    key = 'jobid'
    __oserror__ = Cobalt.Util.FailureMode("QM Connection (job)")
    __function__ = ComponentProxy("queue-manager").get_jobs
    __fields__ = ['nodes', 'location', 'jobid', 'state', 'index',
                  'walltime', 'queue', 'user', 'submittime', 'system_state', 
                  'starttime', 'project' ]

class Queue(ForeignData):
    fields = ForeignData.fields + [
        "name", "state", "policy", "priority"
    ]

    def __init__(self, spec):
        ForeignData.__init__(self, spec)
        spec = spec.copy()
        self.name = spec.pop("name", None)
        self.state = spec.pop("state", None)
        self.policy = spec.pop("policy", None)
        self.priority = spec.pop("priority", 0)
        
        

    def LoadPolicy(self):
        '''Instantiate queue policy modules upon demand'''
        if self.policy not in Cobalt.SchedulerPolicies.names:
            logger.error("Cannot load policy %s for queue %s" % \
                         (self.policy, self.name))
        else:
            pclass = Cobalt.SchedulerPolicies.names[self.policy]
            self.policy = pclass(self.name)


class QueueDict(ForeignDataDict):
    item_cls = Queue
    key = 'name'
    __oserror__ = Cobalt.Util.FailureMode("QM Connection (queue)")
    __function__ = ComponentProxy("queue-manager").get_queues
    __fields__ = ['name', 'state', 'policy', 'priority']

#    def Sync(self):
#        qp = [(q.name, q.policy) for q in self.itervalues()]
#        Cobalt.Data.ForeignDataDict.Sync(self)
#        [q.LoadPolicy() for q in self.itervalues() \
#         if (q.name, q.policy) not in qp]


class BGSched (Component):
    
    implementation = "bgsched"
    name = "scheduler"
    logger = logging.getLogger("Cobalt.Components.scheduler")
    
    _configfields = ['utility_file']
    _config = ConfigParser.ConfigParser()
    _config.read(Cobalt.CONFIG_FILES)
    if not _config._sections.has_key('bgsched'):
        print '''"bgsched" section missing from cobalt config file'''
        sys.exit(1)
    config = _config._sections['bgsched']
    mfields = [field for field in _configfields if not config.has_key(field)]
    if mfields:
        print "Missing option(s) in cobalt config file [bgsched] section: %s" % (" ".join(mfields))
        sys.exit(1)
    if config.get("default_reservation_policy"):
        global DEFAULT_RESERVATION_POLICY
        DEFAULT_RESERVATION_POLICY = config.get("default_reservation_policy")
    
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.reservations = ReservationDict()
        self.queues = QueueDict()
        self.jobs = JobDict()
        self.sched_info = {}
        self.started_jobs = {}
        self.sync_state = Cobalt.Util.FailureMode("Foreign Data Sync")
        self.active = True
        self.user_utility_functions = {}
        self.builtin_utility_functions = {}
    
        self.define_builtin_utility_functions()
        self.define_user_utility_functions()

    def __getstate__(self):
        return {'reservations':self.reservations, 'version':1,
                'active':self.active}
    
    def __setstate__(self, state):
        self.reservations = state['reservations']
        if 'active' in state:
            self.active = state['active']
        else:
            self.active = True
        
        self.queues = QueueDict()
        self.jobs = JobDict()
        self.sched_info = {}
        self.started_jobs = {}
        self.sync_state = Cobalt.Util.FailureMode("Foreign Data Sync")
        self.user_utility_functions = {}
        self.builtin_utility_functions = {}
        
        self.define_builtin_utility_functions()
        self.define_user_utility_functions()


    # order the jobs with biggest utility first
    def utilitycmp(self, tuple1, tuple2):
        return -cmp(tuple1[1], tuple2[1])
    
    def prioritycmp(self, job1, job2):
        """Compare 2 jobs first using queue priority and then first-in, first-out."""
        
        val = cmp(self.queues[job1.queue].priority, self.queues[job2.queue].priority)
        if val == 0:
            return self.fifocmp(job1, job2)
        else:
            # we want the higher priority first
            return -val
        
    def fifocmp (self, job1, job2):
        """Compare 2 jobs for first-in, first-out."""
        
        def fifo_value (job):
            if job.index is not None:
                return int(job.index)
            else:
                return job.jobid
            
        # Implement some simple variations on FIFO scheduling
        # within a particular queue, based on queue policy
        fifoval = cmp(fifo_value(job1), fifo_value(job2))
        if(job1.queue == job2.queue):
            qpolicy = self.queues[job1.queue].policy
            sizeval = cmp(int(job1.nodes), int(job2.nodes))
            wtimeval = cmp(int(job1.walltime), int(job2.walltime))
            if(qpolicy == 'largest-first' and sizeval):
                return -sizeval
            elif(qpolicy == 'smallest-first' and sizeval):
                return sizeval
            elif(qpolicy == 'longest-first' and wtimeval):
                return -wtimeval
            elif(qpolicy == 'shortest-first' and wtimeval):
                return wtimeval
            else:
                return fifoval
        else:
            return fifoval

        return cmp(fifo_value(job1), fifo_value(job2))

    def save_me(self):
        Component.save(self)
    save_me = automatic(save_me)

    def add_reservations (self, specs, user_name):
        self.logger.info("%s adding reservation: %r" % (user_name, specs))
        return self.reservations.q_add(specs)
    add_reservations = exposed(query(add_reservations))

    def del_reservations (self, specs, user_name):
        self.logger.info("%s releasing reservation: %r" % (user_name, specs))
        return self.reservations.q_del(specs)
    del_reservations = exposed(query(del_reservations))

    def get_reservations (self, specs):
        return self.reservations.q_get(specs)
    get_reservations = exposed(query(get_reservations))

    def set_reservations(self, specs, updates, user_name):
        self.logger.info("%s modifying reservation: %r with updates %r" % (user_name, specs, updates))
        def _set_reservations(res, newattr):
            res.update(newattr)
        return self.reservations.q_get(specs, _set_reservations, updates)
    set_reservations = exposed(query(set_reservations))

    def check_reservations(self):
        ret = ""
        reservations = self.reservations.values()
        for i in range(len(reservations)):
            for j in range(i+1, len(reservations)):
                # if at least one reservation is cyclic, we want *that* reservation to be the one getting its overlaps method called
                if reservations[i].cycle is not None:
                    res1 = reservations[i]
                    res2 = reservations[j]
                else:
                    res1 = reservations[j]
                    res2 = reservations[i]

                # we subtract a little bit because the overlaps method isn't really meant to do this
                # it will report warnings when one reservation starts at the same time another ends
                if res1.overlaps(res2.start, res2.duration - 0.00001):
                    # now we need to check for overlap in space
                    results = ComponentProxy("system").get_partitions(
                        [ {'name': p, 'children': '*', 'parents': '*'} for p in res2.partitions.split(":") ]
                    )
                    for p in res1.partitions.split(":"):
                        for r in results:
                            if p==r['name'] or p in r['children'] or p in r['parents']:
                                ret += "Warning: reservation '%s' overlaps reservation '%s'\n" % (res1.name, res2.name)

        return ret
    check_reservations = exposed(check_reservations)

    def sync_data(self):
        started = time.time()
        for item in [self.jobs, self.queues]:
            try:
                item.Sync()
            except (ComponentLookupError, xmlrpclib.Fault):
                # the ForeignDataDicts already include FailureMode stuff
                pass
        # print "took %f seconds for sync_data" % (time.time() - started, )
    sync_data = automatic(sync_data)

    def _run_reservation_jobs (self):
        # handle each reservation separately, as they shouldn't be competing for resources
        for cur_res in self.reservations.itervalues():
            queue = cur_res.queue
            if not (self.queues.has_key(queue) and self.queues[queue].state == 'running'):
                continue
            
            temp_jobs = self.jobs.q_get([{'state':"queued", 'queue':queue}])
            active_jobs = []
            for j in temp_jobs:
                if not self.started_jobs.has_key(j.jobid):
                    active_jobs.append(j)
    
            utility_scores = self._compute_utility_scores(active_jobs, time.time())
            if not utility_scores:
                # if we've got no utility scores, either there were no active_jobs
                # or an error occurred -- either way, give up now
                continue
            utility_scores.sort(self.utilitycmp)
            
            job_location_args = []
            for tup in utility_scores:
                job = tup[0]
                job_location_args.append( 
                    { 'jobid': str(job.jobid), 
                      'nodes': job.nodes, 
                      'queue': job.queue, 
                      'required': cur_res.partitions.split(":"),
                      'utility_score': tup[1],
                      'walltime': job.walltime,
                    } )

            # there's no backfilling in reservations
            try:
                best_partition_dict = ComponentProxy("system").find_job_location(job_location_args, utility_scores[0][2], 0)
            except:
                self.logger.error("failed to connect to system component")
                best_partition_dict = {}
    
            for jobid in best_partition_dict:
                job = self.jobs[int(jobid)]
                self._start_job(job, best_partition_dict[jobid])

    def _start_job(self, job, partition_list):
        cqm = ComponentProxy("queue-manager")
        
        try:
            self.logger.info("trying to start job %d on partition %r" % (job.jobid, partition_list))
            cqm.run_jobs([{'tag':"job", 'jobid':job.jobid}], partition_list)
        except ComponentLookupError:
            self.logger.error("failed to connect to queue manager")
            return

        self.started_jobs[job.jobid] = time.time()


    def _compute_utility_scores (self, active_jobs, current_time):
        utility_scores = []
            
        # tack on a 0 so the list is never empty    
        # max_nodes = max([int(p.size) for p in self.partitions.values()] + [0])
        
        for job in active_jobs:
            utility_name = self.queues[job.queue].policy
            args = {'queued_time':current_time - float(job.submittime), 
                    'wall_time': float(job.walltime), 
                    'size': float(job.nodes),
                    'user_name': job.user,
                    'project': job.project,
                    'queue_priority': int(self.queues[job.queue].priority),
                    #'machine_size': max_nodes,
                    'jobid': int(job.jobid),
                    }
            try:
                if utility_name in self.builtin_utility_functions:
                    utility_func = self.builtin_utility_functions[utility_name]
                else:
                    utility_func = self.user_utility_functions[utility_name]
                utility_func.func_globals.update(args)
                score = utility_func()
            except KeyError:
                # do something sensible when the requested utility function doesn't exist
                # probably go back to the "default" one
                
                # and if we get here, try to fix it and throw away this scheduling iteration
                self.logger.error("cannot find utility function '%s' named by queue '%s'" % (utility_name, job.queue))
                self.user_utility_functions[utility_name] = self.builtin_utility_functions["default"]
                self.logger.error("falling back to 'default' policy to replace '%s'" % utility_name)
                return
            except:
                # do something sensible when the requested utility function explodes
                # probably go back to the "default" one
                
                # and if we get here, try to fix it and throw away this scheduling iteration
                self.logger.error("error while executing utility function '%s' named by queue '%s'" % (utility_name, job.queue), exc_info=True)
                self.user_utility_functions[utility_name] = self.builtin_utility_functions["default"]
                self.logger.error("falling back to 'default' policy to replace '%s'" % utility_name)
                return
            
            if type(score) is not types.TupleType:
                score = (score, 0)
            
            self.sched_info[job.jobid] = str(score)    
            utility_scores.append( (job, ) + score)
        return utility_scores

    def schedule_jobs (self):
        '''look at the queued jobs, and decide which ones to start'''

        started_scheduling = time.time()

        if not self.active:
            return
        # if we're missing information, don't bother trying to schedule jobs
        if not (self.queues.__oserror__.status and self.jobs.__oserror__.status):
            self.sync_state.Fail()
            return
        self.sync_state.Pass()
        
        # clean up the started_jobs cached data
        now = time.time()
        for job_name in self.started_jobs.keys():
            if (now - self.started_jobs[job_name]) > 60:
                del self.started_jobs[job_name]

        # cleanup the sched_info information if a job is no longer listed as "active"
        self.sched_info = {}
        
        # cleanup any reservations which have expired
        for res in self.reservations.values():
            if res.is_over():
                self.logger.info("reservation %s has ended; removing" % res.name)
                self.reservations.q_del([{'name': res.name}])
                
        scriptm = ComponentProxy("script-manager")
        
        try:
            script_locations = [job['location'][0] for job in scriptm.get_jobs([{'location':"*"}])]
        except ComponentLookupError:
            self.logger.error("failed to connect to script manager")
            return

        active_queues = []
        spruce_queues = []
        res_queues = set()
        for item in self.reservations.q_get([{'queue':'*'}]):
            if self.queues.has_key(item.queue):
                if self.queues[item.queue].state == 'running':
                    res_queues.add(item.queue)

        for queue in self.queues.itervalues():
            if queue.name not in res_queues and queue.state == 'running':
                if queue.policy == "high_prio":
                    spruce_queues.append(queue)
                else:
                    active_queues.append(queue)
        
        # handle the reservation jobs that might be ready to go
        self._run_reservation_jobs()

        # figure out stuff about queue equivalence classes
        res_info = {}
        for cur_res in self.reservations.values():
            res_info[cur_res.name] = cur_res.partitions
        try:
            equiv = ComponentProxy("system").find_queue_equivalence_classes(res_info, [q.name for q in active_queues + spruce_queues])
        except:
            self.logger.error("failed to connect to system component")
            return
        
        for eq_class in equiv:
            temp_jobs = self.jobs.q_get([{'state':"queued", 'queue':queue.name} for queue in active_queues if queue.name in eq_class['queues']])
            active_jobs = []
            for j in temp_jobs:
                if not self.started_jobs.has_key(j.jobid):
                    active_jobs.append(j)
    
            temp_jobs = self.jobs.q_get([{'state':"queued", 'queue':queue.name} for queue in spruce_queues if queue.name in eq_class['queues']])
            spruce_jobs = []
            for j in temp_jobs:
                if not self.started_jobs.has_key(j.jobid):
                    spruce_jobs.append(j)
    
            # if there are any pending jobs in high_prio queues, those are the only ones that can start
            if spruce_jobs:
                active_jobs = spruce_jobs
    
            utility_scores = self._compute_utility_scores(active_jobs, now)
            if not utility_scores:
                # if we've got no utility scores, either there were no active_jobs
                # or an error occurred -- either way, go on to the next equivalence class
                continue
            utility_scores.sort(self.utilitycmp)
            
            
            # get the cutoff time for backfilling
            temp_jobs = [job for job in self.jobs.q_get([{'system_state':"running"}]) if job.queue in eq_class['queues']]
            end_times = []
            for job in temp_jobs:
                end_time = float(job.starttime) + 60 * float(job.walltime)
                end_times.append(end_time)
            
            for res_name in eq_class['reservations']:
                cur_res = self.reservations[res_name]

                if not cur_res.cycle:
                    end_time = float(cur_res.start) + float(cur_res.duration)
                else:
                    done_after = float(cur_res.duration) - ((now - float(cur_res.start)) % float(cur_res.cycle))
                    if done_after < 0:
                        done_after += cur_res.cycle
                    end_time = now + done_after
                end_times.append(end_time)
    
            if end_times:
                # add on an extra 2 minutes so that some jobs with the same walltime can start together 
                cut_off = min(end_times) - now + 120
            else:
                # if nothing is running, we can't technically "back fill" and there's just nothing to run
                cut_off = 0

            
            # now smoosh lots of data together to be passed to the allocator in the system component
            job_location_args = []
            for tup in utility_scores:
                job = tup[0]
                forbidden_locations = set(script_locations)
                for res_name in eq_class['reservations']:
                    cur_res = self.reservations[res_name]
                    if cur_res.overlaps(time.time(), 60 * float(job.walltime) + SLOP_TIME):
                        forbidden_locations.update(cur_res.partitions.split(":"))

                job_location_args.append( 
                    { 'jobid': str(job.jobid), 
                      'nodes': job.nodes, 
                      'queue': job.queue, 
                      'forbidden': list(forbidden_locations),
                      'utility_score': tup[1],
                      'walltime': job.walltime,
                    } )

            try:
                best_partition_dict = ComponentProxy("system").find_job_location(job_location_args, utility_scores[0][2], cut_off)
            except:
                self.logger.error("failed to connect to system component", exc_info=True)
                best_partition_dict = {}
    
            for jobid in best_partition_dict:
                job = self.jobs[int(jobid)]
                self._start_job(job, best_partition_dict[jobid])
    

        # print "took %f seconds for scheduling loop" % (time.time() - started_scheduling, )
    schedule_jobs = automatic(schedule_jobs)

    
    def get_sched_info(self):
        """Get information about why jobs aren't running."""
        ret = {}
        for k in self.sched_info:
            ret[str(k)] = self.sched_info[k]
        return ret
    get_sched_info = exposed(get_sched_info)

    def enable(self):
        """Enable scheduling"""
        self.active = True
    enable = exposed(enable)

    def disable(self):
        """Disable scheduling"""
        self.active = False
    disable = exposed(disable)

    def define_user_utility_functions(self):
        self.logger.info("building user utility functions")
        self.user_utility_functions.clear()
        filename = self.config.get("utility_file")
        try:
            f = open(filename)
        except:
            self.logger.error("Can't read utility function definitions from file %s" % self.config.get("utility_file"))
            return
        
        str = f.read()
        
        try:
            code = compile(str, filename, 'exec')
        except:
            self.logger.error("Problem compiling utility function definitions.", exc_info=True)
            return
        
        globals = {'math':math, 'time':time}
        locals = {}
        try:
            exec code in globals, locals
        except:
            self.logger.error("Problem executing utility function definitions.", exc_info=True)
            
        for thing in locals.values():
            if type(thing) is types.FunctionType:
                if thing.func_name in self.builtin_utility_functions:
                    self.logger.error("Attempting to overwrite builtin utility function '%s'.  User version discarded." % thing.func_name)
                else:
                    self.user_utility_functions[thing.func_name] = thing
    define_user_utility_functions = exposed(define_user_utility_functions)
            
    def define_builtin_utility_functions(self):
        self.logger.info("building builtin utility functions")
        self.builtin_utility_functions.clear()
        
        # I think this duplicates cobalt's old scheduling policy
        # higher queue priorities win, with jobid being the tie breaker
        def default():
            val = queue_priority + (1.0/(jobid+1))
            return (val, 0)
    
        def high_prio():
            val = queued_time
            return (val, 0)
    
        self.builtin_utility_functions["default"] = default
        self.builtin_utility_functions["high_prio"] = high_prio
