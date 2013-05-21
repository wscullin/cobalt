import testutils

# ---------------------------------------------------------------------------------
def test_qmove_invalid_option():
    """
    qmove test run: invalid_option
        Old Command Output:
          Usage:
          qmove <queue name> <jobid> <jobid>
          

    """

    args      = """-k"""

    cmdout    = \
"""Usage: qmove.py [options] <queue name> <jobid1> [... <jobidN>]

qmove.py: error: no such option: -k
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       512, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qmove.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qmove_queue_1():
    """
    qmove test run: queue_1
        Old Command Output:
          moved job 1 to queue 'kebra'
          moved job 2 to queue 'kebra'
          moved job 3 to queue 'kebra'
          

    """

    args      = """myq 1 2 3"""

    cmdout    = \
"""get_config_option: Option filters not found in section [cqm]
moved job 1 to queue 'kebra'
moved job 2 to queue 'kebra'
moved job 3 to queue 'kebra'
"""

    stubout   = \
"""
GET_JOBS

jobid:1
nodes:*
notify:*
procs:*
project:*
queue:*
tag:job
user:gooduser
walltime:*
jobid:2
nodes:*
notify:*
procs:*
project:*
queue:*
tag:job
user:gooduser
walltime:*
jobid:3
nodes:*
notify:*
procs:*
project:*
queue:*
tag:job
user:gooduser
walltime:*

SET_JOBS


Original Jobs:

user: gooduser
args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:1
location:/tmp
mode:smp
nodes:512
notify:myemail@gmail.com
outputpath:/tmp
procs:512
project:my_project
queue:jello
score:50
state:user_hold
submittime:60
tag:job
user:land
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:5

New Job Info:

args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:1
location:/tmp
mode:smp
nodes:512
notify:myemail@gmail.com
outputpath:/tmp
procs:512
project:my_project
queue:myq
score:50
state:user_hold
submittime:60
tag:job
user:land
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:5

SET_JOBS


Original Jobs:

user: gooduser
args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:2
location:/tmp
mode:smp
nodes:1024
notify:myemail@gmail.com
outputpath:/tmp
procs:1024
project:my_project
queue:bello
score:55
state:user_hold
submittime:60
tag:job
user:house
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:10

New Job Info:

args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:2
location:/tmp
mode:smp
nodes:1024
notify:myemail@gmail.com
outputpath:/tmp
procs:1024
project:my_project
queue:myq
score:55
state:user_hold
submittime:60
tag:job
user:house
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:10

SET_JOBS


Original Jobs:

user: gooduser
args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:3
location:/tmp
mode:smp
nodes:1536
notify:myemail@gmail.com
outputpath:/tmp
procs:1536
project:my_project
queue:aaa
score:40
state:user_hold
submittime:60
tag:job
user:dog
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:15

New Job Info:

args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:3
location:/tmp
mode:smp
nodes:1536
notify:myemail@gmail.com
outputpath:/tmp
procs:1536
project:my_project
queue:myq
score:40
state:user_hold
submittime:60
tag:job
user:dog
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:15
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qmove.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qmove_queue_2():
    """
    qmove test run: queue_2

    """

    args      = """-d myq 1 2 3"""

    cmdout    = \
"""
qmove.py -d myq 1 2 3

get_config_option: Option filters not found in section [cqm]
component: "queue-manager.get_jobs", defer: False
  get_jobs(
     [{'project': '*', 'queue': '*', 'tag': 'job', 'notify': '*', 'user': 'gooduser', 'nodes': '*', 'walltime': '*', 'procs': '*', 'jobid': 1}, {'project': '*', 'queue': '*', 'tag': 'job', 'notify': '*', 'user': 'gooduser', 'nodes': '*', 'walltime': '*', 'procs': '*', 'jobid': 2}, {'project': '*', 'queue': '*', 'tag': 'job', 'notify': '*', 'user': 'gooduser', 'nodes': '*', 'walltime': '*', 'procs': '*', 'jobid': 3}],
     )


component: "queue-manager.set_jobs", defer: False
  set_jobs(
     [{'errorpath': '/tmp', 'args': '', 'is_active': False, 'geometry': None, 'mode': 'smp', 'outputpath': '/tmp', 'tag': 'job', 'notify': 'myemail@gmail.com', 'has_completed': False, 'procs': 512, 'walltime': 5, 'queue': 'jello', 'envs': {}, 'user_hold': False, 'jobid': 1, 'project': 'my_project', 'submittime': 60, 'state': 'user_hold', 'score': 50, 'location': '/tmp', 'nodes': 512, 'user_list': ['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy'], 'user': 'land'}],
     {'errorpath': '/tmp', 'outputpath': '/tmp', 'tag': 'job', 'notify': 'myemail@gmail.com', 'has_completed': False, 'project': 'my_project', 'envs': {}, 'submittime': 60, 'state': 'user_hold', 'score': 50, 'location': '/tmp', 'nodes': 512, 'args': '', 'is_active': False, 'user': 'land', 'procs': 512, 'walltime': 5, 'geometry': None, 'user_hold': False, 'jobid': 1, 'queue': 'myq', 'mode': 'smp', 'user_list': ['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']},
     gooduser,
     )


component: "queue-manager.set_jobs", defer: False
  set_jobs(
     [{'errorpath': '/tmp', 'args': '', 'is_active': False, 'geometry': None, 'mode': 'smp', 'outputpath': '/tmp', 'tag': 'job', 'notify': 'myemail@gmail.com', 'has_completed': False, 'procs': 1024, 'walltime': 10, 'queue': 'bello', 'envs': {}, 'user_hold': False, 'jobid': 2, 'project': 'my_project', 'submittime': 60, 'state': 'user_hold', 'score': 55, 'location': '/tmp', 'nodes': 1024, 'user_list': ['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy'], 'user': 'house'}],
     {'errorpath': '/tmp', 'outputpath': '/tmp', 'tag': 'job', 'notify': 'myemail@gmail.com', 'has_completed': False, 'project': 'my_project', 'envs': {}, 'submittime': 60, 'state': 'user_hold', 'score': 55, 'location': '/tmp', 'nodes': 1024, 'args': '', 'is_active': False, 'user': 'house', 'procs': 1024, 'walltime': 10, 'geometry': None, 'user_hold': False, 'jobid': 2, 'queue': 'myq', 'mode': 'smp', 'user_list': ['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']},
     gooduser,
     )


component: "queue-manager.set_jobs", defer: False
  set_jobs(
     [{'errorpath': '/tmp', 'args': '', 'is_active': False, 'geometry': None, 'mode': 'smp', 'outputpath': '/tmp', 'tag': 'job', 'notify': 'myemail@gmail.com', 'has_completed': False, 'procs': 1536, 'walltime': 15, 'queue': 'aaa', 'envs': {}, 'user_hold': False, 'jobid': 3, 'project': 'my_project', 'submittime': 60, 'state': 'user_hold', 'score': 40, 'location': '/tmp', 'nodes': 1536, 'user_list': ['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy'], 'user': 'dog'}],
     {'errorpath': '/tmp', 'outputpath': '/tmp', 'tag': 'job', 'notify': 'myemail@gmail.com', 'has_completed': False, 'project': 'my_project', 'envs': {}, 'submittime': 60, 'state': 'user_hold', 'score': 40, 'location': '/tmp', 'nodes': 1536, 'args': '', 'is_active': False, 'user': 'dog', 'procs': 1536, 'walltime': 15, 'geometry': None, 'user_hold': False, 'jobid': 3, 'queue': 'myq', 'mode': 'smp', 'user_list': ['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']},
     gooduser,
     )


moved job 1 to queue 'kebra'
moved job 2 to queue 'kebra'
moved job 3 to queue 'kebra'
"""

    stubout   = \
"""
GET_JOBS

jobid:1
nodes:*
notify:*
procs:*
project:*
queue:*
tag:job
user:gooduser
walltime:*
jobid:2
nodes:*
notify:*
procs:*
project:*
queue:*
tag:job
user:gooduser
walltime:*
jobid:3
nodes:*
notify:*
procs:*
project:*
queue:*
tag:job
user:gooduser
walltime:*

SET_JOBS


Original Jobs:

user: gooduser
args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:1
location:/tmp
mode:smp
nodes:512
notify:myemail@gmail.com
outputpath:/tmp
procs:512
project:my_project
queue:jello
score:50
state:user_hold
submittime:60
tag:job
user:land
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:5

New Job Info:

args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:1
location:/tmp
mode:smp
nodes:512
notify:myemail@gmail.com
outputpath:/tmp
procs:512
project:my_project
queue:myq
score:50
state:user_hold
submittime:60
tag:job
user:land
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:5

SET_JOBS


Original Jobs:

user: gooduser
args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:2
location:/tmp
mode:smp
nodes:1024
notify:myemail@gmail.com
outputpath:/tmp
procs:1024
project:my_project
queue:bello
score:55
state:user_hold
submittime:60
tag:job
user:house
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:10

New Job Info:

args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:2
location:/tmp
mode:smp
nodes:1024
notify:myemail@gmail.com
outputpath:/tmp
procs:1024
project:my_project
queue:myq
score:55
state:user_hold
submittime:60
tag:job
user:house
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:10

SET_JOBS


Original Jobs:

user: gooduser
args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:3
location:/tmp
mode:smp
nodes:1536
notify:myemail@gmail.com
outputpath:/tmp
procs:1536
project:my_project
queue:aaa
score:40
state:user_hold
submittime:60
tag:job
user:dog
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:15

New Job Info:

args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:3
location:/tmp
mode:smp
nodes:1536
notify:myemail@gmail.com
outputpath:/tmp
procs:1536
project:my_project
queue:myq
score:40
state:user_hold
submittime:60
tag:job
user:dog
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:15
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qmove.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qmove_queue_3():
    """
    qmove test run: queue_3
        Old Command Output:
          moved job 2 to queue 'kebra'
          moved job 3 to queue 'kebra'
          moved job 4 to queue 'kebra'
          

    """

    args      = """1 2 3 4"""

    cmdout    = \
"""get_config_option: Option filters not found in section [cqm]
moved job 2 to queue 'kebra'
moved job 3 to queue 'kebra'
moved job 4 to queue 'kebra'
"""

    stubout   = \
"""
GET_JOBS

jobid:2
nodes:*
notify:*
procs:*
project:*
queue:*
tag:job
user:gooduser
walltime:*
jobid:3
nodes:*
notify:*
procs:*
project:*
queue:*
tag:job
user:gooduser
walltime:*
jobid:4
nodes:*
notify:*
procs:*
project:*
queue:*
tag:job
user:gooduser
walltime:*

SET_JOBS


Original Jobs:

user: gooduser
args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:2
location:/tmp
mode:smp
nodes:512
notify:myemail@gmail.com
outputpath:/tmp
procs:512
project:my_project
queue:jello
score:50
state:user_hold
submittime:60
tag:job
user:land
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:5

New Job Info:

args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:2
location:/tmp
mode:smp
nodes:512
notify:myemail@gmail.com
outputpath:/tmp
procs:512
project:my_project
queue:1
score:50
state:user_hold
submittime:60
tag:job
user:land
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:5

SET_JOBS


Original Jobs:

user: gooduser
args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:3
location:/tmp
mode:smp
nodes:1024
notify:myemail@gmail.com
outputpath:/tmp
procs:1024
project:my_project
queue:bello
score:55
state:user_hold
submittime:60
tag:job
user:house
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:10

New Job Info:

args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:3
location:/tmp
mode:smp
nodes:1024
notify:myemail@gmail.com
outputpath:/tmp
procs:1024
project:my_project
queue:1
score:55
state:user_hold
submittime:60
tag:job
user:house
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:10

SET_JOBS


Original Jobs:

user: gooduser
args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:4
location:/tmp
mode:smp
nodes:1536
notify:myemail@gmail.com
outputpath:/tmp
procs:1536
project:my_project
queue:aaa
score:40
state:user_hold
submittime:60
tag:job
user:dog
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:15

New Job Info:

args:
envs:{}
errorpath:/tmp
geometry:None
has_completed:False
is_active:False
jobid:4
location:/tmp
mode:smp
nodes:1536
notify:myemail@gmail.com
outputpath:/tmp
procs:1536
project:my_project
queue:1
score:40
state:user_hold
submittime:60
tag:job
user:dog
user_hold:False
user_list:['james', 'land', 'house', 'dog', 'cat', 'henry', 'king', 'queen', 'girl', 'boy']
walltime:15
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qmove.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_qmove_queu_4():
    """
    qmove test run: queu_4
        Old Command Output:
          jobid must be an integer
          

    """

    args      = """q1 q2 1 2 3"""

    cmdout    = \
"""jobid must be an integer: q2
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('qmove.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result

