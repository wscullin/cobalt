import testutils

# ---------------------------------------------------------------------------------
def test_partadm_version_option():
    """
    partadm test run: version_option
        Old Command Output:
          Cobalt Version: $Version$
          

    """

    args      = """--version"""

    cmdout    = \
"""version: "partadm.py " + $Revision: 1981 $ + , Cobalt  + $Version$
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_help_option_1():
    """
    partadm test run: help_option_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          Options:
            --version             show program's version number and exit
            -h, --help            show this help message and exit
            -a                    add the block to the list of managed blocks
            -d                    remove the block from the list of managed blocks
            -l                    list all blocks and their status
            -r, --recursive       recursively add all child blocks of the specified
                                  blocks in the positional arguments
            --queue=QUEUE         set the queues associated with the target blocks to
                                  this list of queues
            --activate            activate the block for scheduling
            --deactivate          deactivate the block for schedulign
            --enable              enable the running of jobs on the target blocks
            --disable             disable the running of jobs on the target blocks
            --fail                mark the block as though it failed diagnostics
                                  (deprecated)
            --unfail              clear failed diagnostics on a block (deprecated)
            --dump                dump a representation of the system's block state
            --xml                 dump a xml representation of the system's blocks for
                                  simulator usage
            --savestate=SAVESTATE
                                  force the system component to write it's statefile
            --boot-stop           disable booting of any jobs
            --boot-start          enable booting of any jobs
            --boot-status         show whether or not booting is enabled
            -b, --blockinfo       print the detailed state and information for all
                                  requested blocks.
            --pg_list             not implemented yet
            -c, --clean_block     force the block to cleanup and clear all internal
                                  reservations on that resource
          

    """

    args      = """-h"""

    cmdout    = \
"""Usage: partadm.py [-a|-d] part1 part2 (add or del)
Usage: partadm.py -l
Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
Usage: partadm.py --queue=queue1:queue2 part1 part2
Usage: partadm.py --fail part1 part2
Usage: partadm.py --unfail part1 part2
Usage: partadm.py --dump
Usage: partadm.py --xml
Usage: partadm.py --version
Usage: partadm.py --savestate filename
Usage: partadm.py [--boot-stop|--boot-start|--boot-status]

Must supply one of -a or -d or -l or -start or -stop or --queue or -b
Adding "-r" or "--recursive" will add the children of the blocks passed in.


Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -a                    add the block to the list of managed blocks
  -d                    remove the block from the list of managed blocks
  --debug               turn on communication debugging
  -l                    list all blocks and their status
  -r, --recursive       recursively add all child blocks of the specified
                        blocks in the positional arguments
  --queue=QUEUE         set the queues associated with the target blocks to
                        this list of queues
  --activate            activate the block for scheduling
  --deactivate          deactivate the block for schedulign
  --enable              enable the running of jobs on the target blocks
  --disable             disable the running of jobs on the target blocks
  --fail                mark the block as though it failed diagnostics
                        (deprecated)
  --unfail              clear failed diagnostics on a block (deprecated)
  --dump                dump a representation of the system's block state
  --xml                 dump a xml representation of the system's blocks for
                        simulator usage
  --savestate=SAVESTATE
                        force the system component to write it's statefile
  --boot-stop           disable booting of any jobs
  --boot-start          enable booting of any jobs
  --boot-status         show whether or not booting is enabled
  -b, --blockinfo       print the detailed state and information for all
                        requested blocks.
  --pg_list             not implemented yet
  -c, --clean_block     force the block to cleanup and clear all internal
                        reservations on that resource
  -i, --list_io         list information on IOBlock status
  --add_io_block        add an IO Block to the list of managed IO blocks
  --del_io_block        delete an IO Block to the list of managed IO blocks
  --boot_io_block       initiate a boot of the IO Blocks as positional
                        arguments
  --free_io_block       initiate a free of the IO Blocks as positional
                        arguments
  --set_io_autoboot     set an IO block to be automatically booted
  --unset_io_autoboot   stop automatically rebooting an IO block
  --io_autoboot_start   enable IO Block autobooting
  --io_autoboot_stop    disable IO Block autobooting
  --io_autoboot_status  get status of IO Block autobooting
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_help_option_2():
    """
    partadm test run: help_option_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          Options:
            --version             show program's version number and exit
            -h, --help            show this help message and exit
            -a                    add the block to the list of managed blocks
            -d                    remove the block from the list of managed blocks
            -l                    list all blocks and their status
            -r, --recursive       recursively add all child blocks of the specified
                                  blocks in the positional arguments
            --queue=QUEUE         set the queues associated with the target blocks to
                                  this list of queues
            --activate            activate the block for scheduling
            --deactivate          deactivate the block for schedulign
            --enable              enable the running of jobs on the target blocks
            --disable             disable the running of jobs on the target blocks
            --fail                mark the block as though it failed diagnostics
                                  (deprecated)
            --unfail              clear failed diagnostics on a block (deprecated)
            --dump                dump a representation of the system's block state
            --xml                 dump a xml representation of the system's blocks for
                                  simulator usage
            --savestate=SAVESTATE
                                  force the system component to write it's statefile
            --boot-stop           disable booting of any jobs
            --boot-start          enable booting of any jobs
            --boot-status         show whether or not booting is enabled
            -b, --blockinfo       print the detailed state and information for all
                                  requested blocks.
            --pg_list             not implemented yet
            -c, --clean_block     force the block to cleanup and clear all internal
                                  reservations on that resource
          

    """

    args      = """--help"""

    cmdout    = \
"""Usage: partadm.py [-a|-d] part1 part2 (add or del)
Usage: partadm.py -l
Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
Usage: partadm.py --queue=queue1:queue2 part1 part2
Usage: partadm.py --fail part1 part2
Usage: partadm.py --unfail part1 part2
Usage: partadm.py --dump
Usage: partadm.py --xml
Usage: partadm.py --version
Usage: partadm.py --savestate filename
Usage: partadm.py [--boot-stop|--boot-start|--boot-status]

Must supply one of -a or -d or -l or -start or -stop or --queue or -b
Adding "-r" or "--recursive" will add the children of the blocks passed in.


Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -a                    add the block to the list of managed blocks
  -d                    remove the block from the list of managed blocks
  --debug               turn on communication debugging
  -l                    list all blocks and their status
  -r, --recursive       recursively add all child blocks of the specified
                        blocks in the positional arguments
  --queue=QUEUE         set the queues associated with the target blocks to
                        this list of queues
  --activate            activate the block for scheduling
  --deactivate          deactivate the block for schedulign
  --enable              enable the running of jobs on the target blocks
  --disable             disable the running of jobs on the target blocks
  --fail                mark the block as though it failed diagnostics
                        (deprecated)
  --unfail              clear failed diagnostics on a block (deprecated)
  --dump                dump a representation of the system's block state
  --xml                 dump a xml representation of the system's blocks for
                        simulator usage
  --savestate=SAVESTATE
                        force the system component to write it's statefile
  --boot-stop           disable booting of any jobs
  --boot-start          enable booting of any jobs
  --boot-status         show whether or not booting is enabled
  -b, --blockinfo       print the detailed state and information for all
                        requested blocks.
  --pg_list             not implemented yet
  -c, --clean_block     force the block to cleanup and clear all internal
                        reservations on that resource
  -i, --list_io         list information on IOBlock status
  --add_io_block        add an IO Block to the list of managed IO blocks
  --del_io_block        delete an IO Block to the list of managed IO blocks
  --boot_io_block       initiate a boot of the IO Blocks as positional
                        arguments
  --free_io_block       initiate a free of the IO Blocks as positional
                        arguments
  --set_io_autoboot     set an IO block to be automatically booted
  --unset_io_autoboot   stop automatically rebooting an IO block
  --io_autoboot_start   enable IO Block autobooting
  --io_autoboot_stop    disable IO Block autobooting
  --io_autoboot_status  get status of IO Block autobooting
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_no_arg_1():
    """
    partadm test run: no_arg_1

    """

    args      = ''

    cmdout    = \
"""Must supply one of -a or -d or -l or -start or -stop or --queue or -b.
Adding "-r" or "--recursive" will add the children of the blocks passed in.

"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_no_arg_2():
    """
    partadm test run: no_arg_2

    """

    args      = """-a"""

    cmdout    = \
"""At least one partition must be supplied
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_debug():
    """
    partadm test run: debug

    """

    args      = """--debug"""

    cmdout    = \
"""
partadm.py --debug

Must supply one of -a or -d or -l or -start or -stop or --queue or -b.
Adding "-r" or "--recursive" will add the children of the blocks passed in.

"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_1():
    """
    partadm test run: combo_options_1

    """

    args      = """-a -d PART"""

    cmdout    = \
"""Option combinations not allowed with: delete option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_2():
    """
    partadm test run: combo_options_2

    """

    args      = """-a --enable PART"""

    cmdout    = \
"""Option combinations not allowed with: enable option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_3():
    """
    partadm test run: combo_options_3

    """

    args      = """-d --enable PART"""

    cmdout    = \
"""Option combinations not allowed with: enable option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_4():
    """
    partadm test run: combo_options_4

    """

    args      = """--enable --disable PART"""

    cmdout    = \
"""Option combinations not allowed with: disable option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_5():
    """
    partadm test run: combo_options_5

    """

    args      = """--deactivate --activate PART"""

    cmdout    = \
"""Option combinations not allowed with: deactivate option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_6():
    """
    partadm test run: combo_options_6

    """

    args      = """-a --deactivate PART"""

    cmdout    = \
"""Option combinations not allowed with: deactivate option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_7():
    """
    partadm test run: combo_options_7

    """

    args      = """--fail --unfail PART"""

    cmdout    = \
"""Option combinations not allowed with: unfail option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_8():
    """
    partadm test run: combo_options_8

    """

    args      = """--savestate /tmp/savestate -a"""

    cmdout    = \
"""Option combinations not allowed with: savestate option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_9():
    """
    partadm test run: combo_options_9

    """

    args      = """-l --xml"""

    cmdout    = \
"""Option combinations not allowed with: list_blocks option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_10():
    """
    partadm test run: combo_options_10

    """

    args      = """-l --xml"""

    cmdout    = \
"""Option combinations not allowed with: list_blocks option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_11():
    """
    partadm test run: combo_options_11

    """

    args      = """-a --queue q1 PART"""

    cmdout    = \
"""Option combinations not allowed with: queue option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_12():
    """
    partadm test run: combo_options_12

    """

    args      = """--dump --queue q1 PART"""

    cmdout    = \
"""Option combinations not allowed with: dump option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_13():
    """
    partadm test run: combo_options_13

    """

    args      = """--savestate /tmp/s --xml"""

    cmdout    = \
"""Option combinations not allowed with: savestate option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_14():
    """
    partadm test run: combo_options_14

    """

    args      = """-a -c -b PART"""

    cmdout    = \
"""Option combinations not allowed with: blockinfo, clean_block option(s)
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_15():
    """
    partadm test run: combo_options_15
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --list_io
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-A> <-D> <-D> <-_> <-P> <-A> <-R> <-T> <-I> <-T> <-I> <-O> <-N> <-
    > <-
    > <-u> <-s> <-e> <-r> <- > <-n> <-a> <-m> <-e> <-:> <- > <-g> <-o> <-o> <-d> <-u> <-s> <-e> <-r> <-
    > <-
    > <-G> <-E> <-T> <-_> <-I> <-O> <-_> <-B> <-L> <-O> <-C> <-K> <-S> <-
    > <-
    > <-p> <-l> <-i> <-s> <-t> <-:> <- > <-[> <-{> <-'> <-s> <-t> <-a> <-t> <-u> <-s> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-n> <-a> <-m> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-t> <-a> <-t> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-a> <-u> <-t> <-o> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-b> <-l> <-o> <-c> <-k> <-_> <-c> <-o> <-m> <-p> <-u> <-t> <-e> <-s> <-_> <-f> <-o> <-r> <-_> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-i> <-z> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-}> <-]> <-
    > 
    """

    args      = """--list_io -a"""

    cmdout    = \
"""Name  Size  State  CS Status  BlockComputes  Autoreboot
=========================================================
P1    0     idle   OK               x        x         
P2    1     idle   OK               x        x         
P3    2     idle   OK               x        x         
P4    3     idle   OK               x        x         
P5    4     idle   OK               x        x         
P6    5     idle   OK               x        x         
P7    6     idle   OK               x        x         
P8    7     idle   OK               x        x         
P9    8     idle   OK               x        x         
P10   9     idle   OK               x        x         
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_combo_options_16():
    """
    partadm test run: combo_options_16
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --list_io
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-A> <-D> <-D> <-_> <-P> <-A> <-R> <-T> <-I> <-T> <-I> <-O> <-N> <-
    > <-
    > <-u> <-s> <-e> <-r> <- > <-n> <-a> <-m> <-e> <-:> <- > <-g> <-o> <-o> <-d> <-u> <-s> <-e> <-r> <-
    > <-d> <-e> <-p> <-s> <-:> <-[> <-]> <-
    > <-f> <-u> <-n> <-c> <-t> <-i> <-o> <-n> <-a> <-l> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-1> <-
    > <-q> <-u> <-e> <-u> <-e> <-:> <-d> <-e> <-f> <-a> <-u> <-l> <-t> <-
    > <-s> <-c> <-h> <-e> <-d> <-u> <-l> <-e> <-d> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-s> <-i> <-z> <-e> <-:> <-*> <-
    > <-t> <-a> <-g> <-:> <-p> <-a> <-r> <-t> <-i> <-t> <-i> <-o> <-n> <-
    > <-d> <-e> <-p> <-s> <-:> <-[> <-]> <-
    > <-f> <-u> <-n> <-c> <-t> <-i> <-o> <-n> <-a> <-l> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-2> <-
    > <-q> <-u> <-e> <-u> <-e> <-:> <-d> <-e> <-f> <-a> <-u> <-l> <-t> <-
    > <-s> <-c> <-h> <-e> <-d> <-u> <-l> <-e> <-d> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-s> <-i> <-z> <-e> <-:> <-*> <-
    > <-t> <-a> <-g> <-:> <-p> <-a> <-r> <-t> <-i> <-t> <-i> <-o> <-n> <-
    > <-d> <-e> <-p> <-s> <-:> <-[> <-]> <-
    > <-f> <-u> <-n> <-c> <-t> <-i> <-o> <-n> <-a> <-l> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-3> <-
    > <-q> <-u> <-e> <-u> <-e> <-:> <-d> <-e> <-f> <-a> <-u> <-l> <-t> <-
    > <-s> <-c> <-h> <-e> <-d> <-u> <-l> <-e> <-d> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-s> <-i> <-z> <-e> <-:> <-*> <-
    > <-t> <-a> <-g> <-:> <-p> <-a> <-r> <-t> <-i> <-t> <-i> <-o> <-n> <-
    > <-d> <-e> <-p> <-s> <-:> <-[> <-]> <-
    > <-f> <-u> <-n> <-c> <-t> <-i> <-o> <-n> <-a> <-l> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-1> <-
    > <-q> <-u> <-e> <-u> <-e> <-:> <-d> <-e> <-f> <-a> <-u> <-l> <-t> <-
    > <-s> <-c> <-h> <-e> <-d> <-u> <-l> <-e> <-d> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-s> <-i> <-z> <-e> <-:> <-*> <-
    > <-t> <-a> <-g> <-:> <-p> <-a> <-r> <-t> <-i> <-t> <-i> <-o> <-n> <-
    > <-d> <-e> <-p> <-s> <-:> <-[> <-]> <-
    > <-f> <-u> <-n> <-c> <-t> <-i> <-o> <-n> <-a> <-l> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-2> <-
    > <-q> <-u> <-e> <-u> <-e> <-:> <-d> <-e> <-f> <-a> <-u> <-l> <-t> <-
    > <-s> <-c> <-h> <-e> <-d> <-u> <-l> <-e> <-d> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-s> <-i> <-z> <-e> <-:> <-*> <-
    > <-t> <-a> <-g> <-:> <-p> <-a> <-r> <-t> <-i> <-t> <-i> <-o> <-n> <-
    > <-d> <-e> <-p> <-s> <-:> <-[> <-]> <-
    > <-f> <-u> <-n> <-c> <-t> <-i> <-o> <-n> <-a> <-l> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-3> <-
    > <-q> <-u> <-e> <-u> <-e> <-:> <-d> <-e> <-f> <-a> <-u> <-l> <-t> <-
    > <-s> <-c> <-h> <-e> <-d> <-u> <-l> <-e> <-d> <-:> <-F> <-a> <-l> <-s> <-e> <-
    > <-s> <-i> <-z> <-e> <-:> <-*> <-
    > <-t> <-a> <-g> <-:> <-p> <-a> <-r> <-t> <-i> <-t> <-i> <-o> <-n> <-
    > <-
    > <-G> <-E> <-T> <-_> <-I> <-O> <-_> <-B> <-L> <-O> <-C> <-K> <-S> <-
    > <-
    > <-p> <-l> <-i> <-s> <-t> <-:> <- > <-[> <-{> <-'> <-s> <-t> <-a> <-t> <-u> <-s> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-n> <-a> <-m> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-t> <-a> <-t> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-a> <-u> <-t> <-o> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-b> <-l> <-o> <-c> <-k> <-_> <-c> <-o> <-m> <-p> <-u> <-t> <-e> <-s> <-_> <-f> <-o> <-r> <-_> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-i> <-z> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-}> <-]> <-
    > 
    """

    args      = """--list_io -a p1 p2 p3"""

    cmdout    = \
"""Name  Size  State  CS Status  BlockComputes  Autoreboot
=========================================================
P1    0     idle   OK               x        x         
P2    1     idle   OK               x        x         
P3    2     idle   OK               x        x         
P4    3     idle   OK               x        x         
P5    4     idle   OK               x        x         
P6    5     idle   OK               x        x         
P7    6     idle   OK               x        x         
P8    7     idle   OK               x        x         
P9    8     idle   OK               x        x         
P10   9     idle   OK               x        x         
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_add_option_1():
    """
    partadm test run: add_option_1
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """-a -r PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

ADD_PARTITION

user name: gooduser
deps:[]
functional:False
name:PART
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:a
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:a
queue:default
scheduled:False
size:*
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_add_option_2():
    """
    partadm test run: add_option_2
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """-a --recursive PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

ADD_PARTITION

user name: gooduser
deps:[]
functional:False
name:PART
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:a
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:a
queue:default
scheduled:False
size:*
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_add_option_3():
    """
    partadm test run: add_option_3
        Old Command Output:
          ['PART1', 'PART2', 'PART3']
          

    """

    args      = """-a PART1 PART2 PART3"""

    cmdout    = \
"""['PART1', 'PART2', 'PART3']
"""

    stubout   = \
"""
ADD_PARTITION

user name: gooduser
deps:[]
functional:False
name:PART1
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART2
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART3
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART1
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART2
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART3
queue:default
scheduled:False
size:*
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_add_option_4():
    """
    partadm test run: add_option_4

    """

    args      = """-a -b PART1 PART2"""

    cmdout    = \
"""Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
ADD_PARTITION

user name: gooduser
deps:[]
functional:False
name:PART1
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART2
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART1
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART2
queue:default
scheduled:False
size:*
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_add_option_5():
    """
    partadm test run: add_option_5
        Old Command Output:
          Initiating cleanup on block PART1
          Initiating cleanup on block PART2
          

    """

    args      = """-a -c PART1 PART2"""

    cmdout    = \
"""Initiating cleanup on block PART1
Initiating cleanup on block PART2
"""

    stubout   = \
"""
ADD_PARTITION

user name: gooduser
deps:[]
functional:False
name:PART1
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART2
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART1
queue:default
scheduled:False
size:*
tag:partition
deps:[]
functional:False
name:PART2
queue:default
scheduled:False
size:*
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: PART1
var2 : None
whoami: gooduser

SET_CLEANING

part: PART2
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_delete_option_1():
    """
    partadm test run: delete_option_1
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """-d -r PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

DEL_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_delete_option_2():
    """
    partadm test run: delete_option_2
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """-d --recursive PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

DEL_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_delete_option_3():
    """
    partadm test run: delete_option_3
        Old Command Output:
          ['PART1', 'PART2', 'PART3']
          

    """

    args      = """-d PART1 PART2 PART3"""

    cmdout    = \
"""['PART1', 'PART2', 'PART3']
"""

    stubout   = \
"""
DEL_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_delete_option_4():
    """
    partadm test run: delete_option_4

    """

    args      = """-d -b PART1 PART2"""

    cmdout    = \
"""Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
DEL_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
name:PART1
tag:partition
name:PART2
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_delete_option_5():
    """
    partadm test run: delete_option_5
        Old Command Output:
          Initiating cleanup on block PART1
          Initiating cleanup on block PART2
          

    """

    args      = """-d -c PART1 PART2"""

    cmdout    = \
"""Initiating cleanup on block PART1
Initiating cleanup on block PART2
"""

    stubout   = \
"""
DEL_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
name:PART1
tag:partition
name:PART2
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: PART1
var2 : None
whoami: gooduser

SET_CLEANING

part: PART2
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_enable_option_1():
    """
    partadm test run: enable_option_1
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--enable -r PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

SET_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
scheduled:True
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_enable_option_2():
    """
    partadm test run: enable_option_2
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--enable --recursive PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

SET_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
scheduled:True
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_enable_option_3():
    """
    partadm test run: enable_option_3
        Old Command Output:
          ['PART1', 'PART2', 'PART3']
          

    """

    args      = """--enable PART1 PART2 PART3"""

    cmdout    = \
"""['PART1', 'PART2', 'PART3']
"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
scheduled:True
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_enable_option_4():
    """
    partadm test run: enable_option_4

    """

    args      = """--enable -b PART1 PART2"""

    cmdout    = \
"""Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
scheduled:True
name:PART1
tag:partition
name:PART2
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_enable_option_5():
    """
    partadm test run: enable_option_5
        Old Command Output:
          Initiating cleanup on block PART1
          Initiating cleanup on block PART2
          

    """

    args      = """--enable -c PART1 PART2"""

    cmdout    = \
"""Initiating cleanup on block PART1
Initiating cleanup on block PART2
"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
scheduled:True
name:PART1
tag:partition
name:PART2
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: PART1
var2 : None
whoami: gooduser

SET_CLEANING

part: PART2
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_disable_option_1():
    """
    partadm test run: disable_option_1
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--disable -r PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

SET_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
scheduled:False
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_disable_option_2():
    """
    partadm test run: disable_option_2
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--disable --recursive PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

SET_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
scheduled:False
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_disable_option_3():
    """
    partadm test run: disable_option_3
        Old Command Output:
          ['PART1', 'PART2', 'PART3']
          

    """

    args      = """--disable PART1 PART2 PART3"""

    cmdout    = \
"""['PART1', 'PART2', 'PART3']
"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
scheduled:False
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_disable_option_4():
    """
    partadm test run: disable_option_4

    """

    args      = """--disable -b PART1 PART2"""

    cmdout    = \
"""Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
scheduled:False
name:PART1
tag:partition
name:PART2
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_disable_option_5():
    """
    partadm test run: disable_option_5
        Old Command Output:
          Initiating cleanup on block PART1
          Initiating cleanup on block PART2
          

    """

    args      = """--disable -c PART1 PART2"""

    cmdout    = \
"""Initiating cleanup on block PART1
Initiating cleanup on block PART2
"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
scheduled:False
name:PART1
tag:partition
name:PART2
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: PART1
var2 : None
whoami: gooduser

SET_CLEANING

part: PART2
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_activate_option_1():
    """
    partadm test run: activate_option_1
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--activate -r PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

SET_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
functional:True
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_activate_option_2():
    """
    partadm test run: activate_option_2
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--activate --recursive PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

SET_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
functional:True
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_activate_option_3():
    """
    partadm test run: activate_option_3
        Old Command Output:
          ['PART1', 'PART2', 'PART3']
          

    """

    args      = """--activate PART1 PART2 PART3"""

    cmdout    = \
"""['PART1', 'PART2', 'PART3']
"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
functional:True
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_activate_option_4():
    """
    partadm test run: activate_option_4

    """

    args      = """--activate -b PART1 PART2"""

    cmdout    = \
"""Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
functional:True
name:PART1
tag:partition
name:PART2
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_activate_option_5():
    """
    partadm test run: activate_option_5
        Old Command Output:
          Initiating cleanup on block PART1
          Initiating cleanup on block PART2
          

    """

    args      = """--activate -c PART1 PART2"""

    cmdout    = \
"""Initiating cleanup on block PART1
Initiating cleanup on block PART2
"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
functional:True
name:PART1
tag:partition
name:PART2
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: PART1
var2 : None
whoami: gooduser

SET_CLEANING

part: PART2
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_deactivate_option_1():
    """
    partadm test run: deactivate_option_1
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--deactivate -r PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

SET_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
functional:False
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_deactivate_option_2():
    """
    partadm test run: deactivate_option_2
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--deactivate --recursive PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

SET_PARTITION

user name: gooduser
name:PART
tag:partition
name:a
tag:partition
functional:False
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_deactivate_option_3():
    """
    partadm test run: deactivate_option_3
        Old Command Output:
          ['PART1', 'PART2', 'PART3']
          

    """

    args      = """--deactivate PART1 PART2 PART3"""

    cmdout    = \
"""['PART1', 'PART2', 'PART3']
"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
functional:False
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_deactivate_option_4():
    """
    partadm test run: deactivate_option_4

    """

    args      = """--deactivate -b PART1 PART2"""

    cmdout    = \
"""Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
functional:False
name:PART1
tag:partition
name:PART2
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_deactivate_option_5():
    """
    partadm test run: deactivate_option_5
        Old Command Output:
          Initiating cleanup on block PART1
          Initiating cleanup on block PART2
          

    """

    args      = """--deactivate -c PART1 PART2"""

    cmdout    = \
"""Initiating cleanup on block PART1
Initiating cleanup on block PART2
"""

    stubout   = \
"""
SET_PARTITION

user name: gooduser
name:PART1
tag:partition
name:PART2
tag:partition
functional:False
name:PART1
tag:partition
name:PART2
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: PART1
var2 : None
whoami: gooduser

SET_CLEANING

part: PART2
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_fail_option_1():
    """
    partadm test run: fail_option_1
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--fail -r PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

FAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART'}, {'tag': 'partition', 'name': 'a'}]
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_fail_option_2():
    """
    partadm test run: fail_option_2
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--fail --recursive PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

FAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART'}, {'tag': 'partition', 'name': 'a'}]
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_fail_option_3():
    """
    partadm test run: fail_option_3
        Old Command Output:
          ['PART1', 'PART2', 'PART3']
          

    """

    args      = """--fail PART1 PART2 PART3"""

    cmdout    = \
"""['PART1', 'PART2', 'PART3']
"""

    stubout   = \
"""
FAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART1'}, {'tag': 'partition', 'name': 'PART2'}, {'tag': 'partition', 'name': 'PART3'}]
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_fail_option_4():
    """
    partadm test run: fail_option_4

    """

    args      = """--fail -b PART1 PART2"""

    cmdout    = \
"""Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
FAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART1'}, {'tag': 'partition', 'name': 'PART2'}]
name:PART1
tag:partition
name:PART2
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_fail_option_5():
    """
    partadm test run: fail_option_5
        Old Command Output:
          Initiating cleanup on block PART1
          Initiating cleanup on block PART2
          

    """

    args      = """--fail -c PART1 PART2"""

    cmdout    = \
"""Initiating cleanup on block PART1
Initiating cleanup on block PART2
"""

    stubout   = \
"""
FAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART1'}, {'tag': 'partition', 'name': 'PART2'}]
name:PART1
tag:partition
name:PART2
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: PART1
var2 : None
whoami: gooduser

SET_CLEANING

part: PART2
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_unfail_option_1():
    """
    partadm test run: unfail_option_1
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--unfail -r PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

UNFAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART'}, {'tag': 'partition', 'name': 'a'}]
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_unfail_option_2():
    """
    partadm test run: unfail_option_2
        Old Command Output:
          ['PART', 'a']
          

    """

    args      = """--unfail --recursive PART"""

    cmdout    = \
"""['PART', 'a']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'PART', 'children_list': '*'}]

UNFAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART'}, {'tag': 'partition', 'name': 'a'}]
name:PART
tag:partition
name:a
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_unfail_option_3():
    """
    partadm test run: unfail_option_3
        Old Command Output:
          ['PART1', 'PART2', 'PART3']
          

    """

    args      = """--unfail PART1 PART2 PART3"""

    cmdout    = \
"""['PART1', 'PART2', 'PART3']
"""

    stubout   = \
"""
UNFAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART1'}, {'tag': 'partition', 'name': 'PART2'}, {'tag': 'partition', 'name': 'PART3'}]
name:PART1
tag:partition
name:PART2
tag:partition
name:PART3
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_unfail_option_4():
    """
    partadm test run: unfail_option_4

    """

    args      = """--unfail -b PART1 PART2"""

    cmdout    = \
"""Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: PART2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
UNFAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART1'}, {'tag': 'partition', 'name': 'PART2'}]
name:PART1
tag:partition
name:PART2
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'PART2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'PART2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_unfail_option_5():
    """
    partadm test run: unfail_option_5
        Old Command Output:
          Initiating cleanup on block PART1
          Initiating cleanup on block PART2
          

    """

    args      = """--unfail -c PART1 PART2"""

    cmdout    = \
"""Initiating cleanup on block PART1
Initiating cleanup on block PART2
"""

    stubout   = \
"""
UNFAIL_PARTITION

user name: gooduser
part list: [{'tag': 'partition', 'name': 'PART1'}, {'tag': 'partition', 'name': 'PART2'}]
name:PART1
tag:partition
name:PART2
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: PART1
var2 : None
whoami: gooduser

SET_CLEANING

part: PART2
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_savestate_option_1():
    """
    partadm test run: savestate_option_1
        Old Command Output:
          directory /bad does not exist
          

    """

    args      = """--savestate /bad/save"""

    cmdout    = \
"""directory /bad/save does not exist
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_savestate_option_2():
    """
    partadm test run: savestate_option_2
        Old Command Output:
          [{'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}]
          

    """

    args      = """--savestate /tmp/save p1"""

    cmdout    = \
"""[{'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}]
"""

    stubout   = \
"""
SAVE

filename:/tmp/save
plist: [{'name': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_savestate_option_3():
    """
    partadm test run: savestate_option_3
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: --savestate option requires an argument
          

    """

    args      = """--savestate"""

    cmdout    = \
"""Usage: partadm.py [-a|-d] part1 part2 (add or del)
Usage: partadm.py -l
Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
Usage: partadm.py --queue=queue1:queue2 part1 part2
Usage: partadm.py --fail part1 part2
Usage: partadm.py --unfail part1 part2
Usage: partadm.py --dump
Usage: partadm.py --xml
Usage: partadm.py --version
Usage: partadm.py --savestate filename
Usage: partadm.py [--boot-stop|--boot-start|--boot-status]

Must supply one of -a or -d or -l or -start or -stop or --queue or -b
Adding "-r" or "--recursive" will add the children of the blocks passed in.


partadm.py: error: --savestate option requires an argument
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       512, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_savestate_option_4():
    """
    partadm test run: savestate_option_4
        Old Command Output:
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          

    """

    args      = """--savestate /tmp/save -c p1"""

    cmdout    = \
"""Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
"""

    stubout   = \
"""
SAVE

filename:/tmp/save
plist: [{'name': '*'}]

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_savestate_option_5():
    """
    partadm test run: savestate_option_5

    """

    args      = """--savestate /tmp/save -b p1"""

    cmdout    = \
"""Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
SAVE

filename:/tmp/save
plist: [{'name': '*'}]

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_xml_option_1():
    """
    partadm test run: xml_option_1
        Old Command Output:
          ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
          

    """

    args      = """--xml"""

    cmdout    = \
"""['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
"""

    stubout   = \
"""
GENERATE_XML

name:*
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_xml_option_2():
    """
    partadm test run: xml_option_2
        Old Command Output:
          ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
          

    """

    args      = """--xml p1"""

    cmdout    = \
"""['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
"""

    stubout   = \
"""
GENERATE_XML

name:*
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_xml_option_3():
    """
    partadm test run: xml_option_3
        Old Command Output:
          ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
          

    """

    args      = """--xml --recursive p1"""

    cmdout    = \
"""['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'p1', 'children_list': '*'}]

GENERATE_XML

name:*
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_xml_option_4():
    """
    partadm test run: xml_option_4

    """

    args      = """--xml --blockinfo"""

    cmdout    = \
"""Name: P1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P3
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P4
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P5
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P6
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P7
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P8
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P9
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P10
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P3
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P4
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P5
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P6
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P7
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P8
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P9
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P10
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
GENERATE_XML

name:*

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P3', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P4', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P5', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P6', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P7', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P8', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P9', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P10', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P3', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P4', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P5', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P6', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P7', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P8', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P9', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P10', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_xml_option_5():
    """
    partadm test run: xml_option_5
        Old Command Output:
          Initiating cleanup on block P1
          Initiating cleanup on block P2
          Initiating cleanup on block P3
          Initiating cleanup on block P4
          Initiating cleanup on block P5
          Initiating cleanup on block P6
          Initiating cleanup on block P7
          Initiating cleanup on block P8
          Initiating cleanup on block P9
          Initiating cleanup on block P10
          

    """

    args      = """--xml --clean_block"""

    cmdout    = \
"""Initiating cleanup on block P1
Initiating cleanup on block P2
Initiating cleanup on block P3
Initiating cleanup on block P4
Initiating cleanup on block P5
Initiating cleanup on block P6
Initiating cleanup on block P7
Initiating cleanup on block P8
Initiating cleanup on block P9
Initiating cleanup on block P10
"""

    stubout   = \
"""
GENERATE_XML

name:*

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: P1
var2 : None
whoami: gooduser

SET_CLEANING

part: P2
var2 : None
whoami: gooduser

SET_CLEANING

part: P3
var2 : None
whoami: gooduser

SET_CLEANING

part: P4
var2 : None
whoami: gooduser

SET_CLEANING

part: P5
var2 : None
whoami: gooduser

SET_CLEANING

part: P6
var2 : None
whoami: gooduser

SET_CLEANING

part: P7
var2 : None
whoami: gooduser

SET_CLEANING

part: P8
var2 : None
whoami: gooduser

SET_CLEANING

part: P9
var2 : None
whoami: gooduser

SET_CLEANING

part: P10
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_xml_option_6():
    """
    partadm test run: xml_option_6

    """

    args      = """--xml --recursive --blockinfo"""

    cmdout    = \
"""Name: P1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P3
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P4
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P5
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P6
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P7
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P8
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P9
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P10
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P2
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P3
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P4
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P5
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P6
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P7
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P8
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P9
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: P10
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

GENERATE_XML

name:*

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P2', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P3', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P4', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P5', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P6', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P7', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P8', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P9', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'P10', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P2', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P3', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P4', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P5', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P6', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P7', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P8', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P9', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'P10', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_xml_option_7():
    """
    partadm test run: xml_option_7
        Old Command Output:
          Initiating cleanup on block P1
          Initiating cleanup on block P2
          Initiating cleanup on block P3
          Initiating cleanup on block P4
          Initiating cleanup on block P5
          Initiating cleanup on block P6
          Initiating cleanup on block P7
          Initiating cleanup on block P8
          Initiating cleanup on block P9
          Initiating cleanup on block P10
          

    """

    args      = """--xml --recursive --clean_block"""

    cmdout    = \
"""Initiating cleanup on block P1
Initiating cleanup on block P2
Initiating cleanup on block P3
Initiating cleanup on block P4
Initiating cleanup on block P5
Initiating cleanup on block P6
Initiating cleanup on block P7
Initiating cleanup on block P8
Initiating cleanup on block P9
Initiating cleanup on block P10
"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

GENERATE_XML

name:*

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: P1
var2 : None
whoami: gooduser

SET_CLEANING

part: P2
var2 : None
whoami: gooduser

SET_CLEANING

part: P3
var2 : None
whoami: gooduser

SET_CLEANING

part: P4
var2 : None
whoami: gooduser

SET_CLEANING

part: P5
var2 : None
whoami: gooduser

SET_CLEANING

part: P6
var2 : None
whoami: gooduser

SET_CLEANING

part: P7
var2 : None
whoami: gooduser

SET_CLEANING

part: P8
var2 : None
whoami: gooduser

SET_CLEANING

part: P9
var2 : None
whoami: gooduser

SET_CLEANING

part: P10
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_queue_option_1():
    """
    partadm test run: queue_option_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: --queue option requires an argument
          

    """

    args      = """--queue"""

    cmdout    = \
"""Usage: partadm.py [-a|-d] part1 part2 (add or del)
Usage: partadm.py -l
Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
Usage: partadm.py --queue=queue1:queue2 part1 part2
Usage: partadm.py --fail part1 part2
Usage: partadm.py --unfail part1 part2
Usage: partadm.py --dump
Usage: partadm.py --xml
Usage: partadm.py --version
Usage: partadm.py --savestate filename
Usage: partadm.py [--boot-stop|--boot-start|--boot-status]

Must supply one of -a or -d or -l or -start or -stop or --queue or -b
Adding "-r" or "--recursive" will add the children of the blocks passed in.


partadm.py: error: --queue option requires an argument
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       512, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_queue_option_2():
    """
    partadm test run: queue_option_2
        Old Command Output:
          'q1' is not an existing queue
          'q2' is not an existing queue
          

    """

    args      = """--queue q1:q2 p1 p2 p3"""

    cmdout    = \
"""'q1' is not an existing queue
'q2' is not an existing queue
"""

    stubout   = \
"""
GET_QUEUES

name:*
tag:queue
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_queue_option_3():
    """
    partadm test run: queue_option_3
        Old Command Output:
          ['p1']
          

    """

    args      = """--queue kebra:bbb:myq p1"""

    cmdout    = \
"""['p1']
"""

    stubout   = \
"""
GET_QUEUES

name:*
tag:queue

SET_PARTITION

user name: gooduser
name:p1
tag:partition
queue:kebra:bbb:myq
name:p1
tag:partition
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_queue_option_4():
    """
    partadm test run: queue_option_4
        Old Command Output:
          Initiating cleanup on block p1
          

    """

    args      = """--queue kebra:bbb:myq -c p1"""

    cmdout    = \
"""Initiating cleanup on block p1
"""

    stubout   = \
"""
GET_QUEUES

name:*
tag:queue

SET_PARTITION

user name: gooduser
name:p1
tag:partition
queue:kebra:bbb:myq
name:p1
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: p1
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_queue_option_5():
    """
    partadm test run: queue_option_5

    """

    args      = """--queue kebra:bbb:myq -b p1"""

    cmdout    = \
"""Name: p1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: p1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
GET_QUEUES

name:*
tag:queue

SET_PARTITION

user name: gooduser
name:p1
tag:partition
queue:kebra:bbb:myq
name:p1
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'p1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'p1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_queue_option_6():
    """
    partadm test run: queue_option_6

    """

    args      = """--queue kebra:bbb -r -b p1"""

    cmdout    = \
"""Name: p1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: a
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: p1
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: a
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'p1', 'children_list': '*'}]

GET_QUEUES

name:*
tag:queue

SET_PARTITION

user name: gooduser
name:p1
tag:partition
name:a
tag:partition
queue:kebra:bbb
name:p1
tag:partition
name:a
tag:partition

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'p1', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': 'a', 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'p1', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': 'a', 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_queue_option_7():
    """
    partadm test run: queue_option_7
        Old Command Output:
          Initiating cleanup on block p1
          Initiating cleanup on block a
          

    """

    args      = """--queue kebra:bbb -r -c p1"""

    cmdout    = \
"""Initiating cleanup on block p1
Initiating cleanup on block a
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'p1', 'children_list': '*'}]

GET_QUEUES

name:*
tag:queue

SET_PARTITION

user name: gooduser
name:p1
tag:partition
name:a
tag:partition
queue:kebra:bbb
name:p1
tag:partition
name:a
tag:partition

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: p1
var2 : None
whoami: gooduser

SET_CLEANING

part: a
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_dump_option_1():
    """
    partadm test run: dump_option_1
        Old Command Output:
          [{'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}]
          

    """

    args      = """--dump"""

    cmdout    = \
"""[{'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}]
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'scheduled': '*', 'queue': '*', 'state': '*', 'tag': 'partition', 'name': '*', 'deps': '*', 'functional': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_dump_option_2():
    """
    partadm test run: dump_option_2
        Old Command Output:
          [{'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}]
          

    """

    args      = """--dump p1"""

    cmdout    = \
"""[{'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}]
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'scheduled': '*', 'queue': '*', 'state': '*', 'tag': 'partition', 'name': '*', 'deps': '*', 'functional': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_dump_option_3():
    """
    partadm test run: dump_option_3
        Old Command Output:
          [{'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}]
          

    """

    args      = """--dump --recursive p1"""

    cmdout    = \
"""[{'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}]
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'p1', 'children_list': '*'}]

GET_PARTITIONS

plist: [{'scheduled': '*', 'queue': '*', 'state': '*', 'tag': 'partition', 'name': '*', 'deps': '*', 'functional': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_dump_option_4():
    """
    partadm test run: dump_option_4

    """

    args      = """--dump --blockinfo"""

    cmdout    = \
"""Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'scheduled': '*', 'queue': '*', 'state': '*', 'tag': 'partition', 'name': '*', 'deps': '*', 'functional': '*', 'size': '*'}]

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_dump_option_5():
    """
    partadm test run: dump_option_5
        Old Command Output:
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          

    """

    args      = """--dump --clean_block"""

    cmdout    = \
"""Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'scheduled': '*', 'queue': '*', 'state': '*', 'tag': 'partition', 'name': '*', 'deps': '*', 'functional': '*', 'size': '*'}]

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_dump_option_6():
    """
    partadm test run: dump_option_6

    """

    args      = """--dump --recursive --blockinfo"""

    cmdout    = \
"""Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 0
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : kebra
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 1
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : jello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 2
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bello
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 3
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : aaa
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 4
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : bbb
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 5
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : hhh
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 6
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : dito
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 7
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : myq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 8
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : yours
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

Name: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
    scheduled                 : True
    status                    : OK
    functional                : True
    draining                  : False
    passthrough_blocks        : A
    children                  : a
    size                      : 9
    node_geometry             : ['48', '48', '48', '48', '48']
    state                     : idle
    queue                     : zq
    relatives                 : ['b']
    parents                   : a, b, c
    block_computes_for_reboot : True
    autoreboot                : True

"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

GET_PARTITIONS

plist: [{'scheduled': '*', 'queue': '*', 'state': '*', 'tag': 'partition', 'name': '*', 'deps': '*', 'functional': '*', 'size': '*'}]

GET_BLOCKS

plist: [{'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}, {'freeing': '*', 'extents': '*', 'corner_node': '*', 'wiring_conflict_list': '*', 'draining': '*', 'passthrough_blocks': '*', 'backfill_time': '*', 'children': '*', 'io_node_list': '*', 'size': '*', 'node_geometry': '*', 'node_list': '*', 'state': '*', 'parents': '*', 'wire_list': '*', 'cleanup_pending': '*', 'scheduled': '*', 'block_type': '*', 'used_by': '*', 'reserved_by': '*', 'node_card_list': '*', 'midplane_list': '*', 'funcitonal': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'midplane_geometry': '*', 'passthrough_midplane_list': '*', 'queue': '*', 'subblock_parent': '*', 'reserved_until': '*'}]

GET_IO_BLOCKS

plist: [{'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}, {'status': '*', 'state': '*', 'autoreboot': '*', 'name': {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}, 'io_drawer_list': '*', 'block_computes_for_reboot': '*', 'io_node_list': '*', 'size': '*'}]
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_dump_option_7():
    """
    partadm test run: dump_option_7
        Old Command Output:
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
          

    """

    args      = """--dump --recursive --clean_block"""

    cmdout    = \
"""Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
Initiating cleanup on block {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

GET_PARTITIONS

plist: [{'scheduled': '*', 'queue': '*', 'state': '*', 'tag': 'partition', 'name': '*', 'deps': '*', 'functional': '*', 'size': '*'}]

SCHED_STATUS


BOOTING_STATUS


SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 0, 'name': 'P1', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'kebra', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 1, 'name': 'P2', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'jello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 2, 'name': 'P3', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bello', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 3, 'name': 'P4', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'aaa', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 4, 'name': 'P5', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'bbb', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 5, 'name': 'P6', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'hhh', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 6, 'name': 'P7', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'dito', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 7, 'name': 'P8', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'myq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 8, 'name': 'P9', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'yours', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser

SET_CLEANING

part: {'scheduled': True, 'status': 'OK', 'functional': True, 'draining': False, 'passthrough_blocks': ['A'], 'children': ['a'], 'size': 9, 'name': 'P10', 'node_geometry': ['48', '48', '48', '48', '48'], 'state': 'idle', 'queue': 'zq', 'relatives': ['b'], 'parents': ['a', 'b', 'c'], 'block_computes_for_reboot': True, 'autoreboot': True}
var2 : None
whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_stop_option_1():
    """
    partadm test run: boot_stop_option_1
        Old Command Output:
          Halting booting: halting scheduling is advised
          

    """

    args      = """--boot-stop"""

    cmdout    = \
"""Halting booting: halting scheduling is advised
"""

    stubout   = \
"""
HALT_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_stop_option_2():
    """
    partadm test run: boot_stop_option_2
        Old Command Output:
          Halting booting: halting scheduling is advised
          

    """

    args      = """--boot-stop p1"""

    cmdout    = \
"""Halting booting: halting scheduling is advised
"""

    stubout   = \
"""
HALT_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_stop_option_3():
    """
    partadm test run: boot_stop_option_3
        Old Command Output:
          Halting booting: halting scheduling is advised
          

    """

    args      = """--boot-stop --recursive p1"""

    cmdout    = \
"""Halting booting: halting scheduling is advised
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'p1', 'children_list': '*'}]

HALT_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_stop_option_4():
    """
    partadm test run: boot_stop_option_4
        Old Command Output:
          Halting booting: halting scheduling is advised
          

    """

    args      = """--boot-stop --blockinfo"""

    cmdout    = \
"""Halting booting: halting scheduling is advised
"""

    stubout   = \
"""
HALT_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_stop_option_5():
    """
    partadm test run: boot_stop_option_5
        Old Command Output:
          Halting booting: halting scheduling is advised
          

    """

    args      = """--boot-stop --clean_block"""

    cmdout    = \
"""Halting booting: halting scheduling is advised
"""

    stubout   = \
"""
HALT_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_stop_option_6():
    """
    partadm test run: boot_stop_option_6
        Old Command Output:
          Halting booting: halting scheduling is advised
          

    """

    args      = """--boot-stop --recursive --blockinfo"""

    cmdout    = \
"""Halting booting: halting scheduling is advised
"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

HALT_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_stop_option_7():
    """
    partadm test run: boot_stop_option_7
        Old Command Output:
          Halting booting: halting scheduling is advised
          

    """

    args      = """--boot-stop --recursive --clean_block"""

    cmdout    = \
"""Halting booting: halting scheduling is advised
"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

HALT_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_start_option_1():
    """
    partadm test run: boot_start_option_1
        Old Command Output:
          Enabling booting
          

    """

    args      = """--boot-start"""

    cmdout    = \
"""Enabling booting
"""

    stubout   = \
"""
RESUME_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_start_option_2():
    """
    partadm test run: boot_start_option_2
        Old Command Output:
          Enabling booting
          

    """

    args      = """--boot-start p1"""

    cmdout    = \
"""Enabling booting
"""

    stubout   = \
"""
RESUME_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_start_option_3():
    """
    partadm test run: boot_start_option_3
        Old Command Output:
          Enabling booting
          

    """

    args      = """--boot-start --recursive p1"""

    cmdout    = \
"""Enabling booting
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'p1', 'children_list': '*'}]

RESUME_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_start_option_4():
    """
    partadm test run: boot_start_option_4
        Old Command Output:
          Enabling booting
          

    """

    args      = """--boot-start --blockinfo"""

    cmdout    = \
"""Enabling booting
"""

    stubout   = \
"""
RESUME_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_start_option_5():
    """
    partadm test run: boot_start_option_5
        Old Command Output:
          Enabling booting
          

    """

    args      = """--boot-start --clean_block"""

    cmdout    = \
"""Enabling booting
"""

    stubout   = \
"""
RESUME_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_start_option_6():
    """
    partadm test run: boot_start_option_6
        Old Command Output:
          Enabling booting
          

    """

    args      = """--boot-start --recursive --blockinfo"""

    cmdout    = \
"""Enabling booting
"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

RESUME_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_start_option_7():
    """
    partadm test run: boot_start_option_7
        Old Command Output:
          Enabling booting
          

    """

    args      = """--boot-start --recursive --clean_block"""

    cmdout    = \
"""Enabling booting
"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

RESUME_BOOTING

whoami: gooduser
"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_status_option_1():
    """
    partadm test run: boot_status_option_1
        Old Command Output:
          Block Booting: ENABLED
          

    """

    args      = """--boot-status"""

    cmdout    = \
"""Block Booting: ENABLED
"""

    stubout   = \
"""
BOOTING_STATUS

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_status_option_2():
    """
    partadm test run: boot_status_option_2
        Old Command Output:
          Block Booting: ENABLED
          

    """

    args      = """--boot-status p1"""

    cmdout    = \
"""Block Booting: ENABLED
"""

    stubout   = \
"""
BOOTING_STATUS

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_status_option_3():
    """
    partadm test run: boot_status_option_3
        Old Command Output:
          Block Booting: ENABLED
          

    """

    args      = """--boot-status --recursive p1"""

    cmdout    = \
"""Block Booting: ENABLED
"""

    stubout   = \
"""
GET_PARTITIONS

plist: [{'tag': 'partition', 'name': 'p1', 'children_list': '*'}]

BOOTING_STATUS

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_status_option_4():
    """
    partadm test run: boot_status_option_4
        Old Command Output:
          Block Booting: ENABLED
          

    """

    args      = """--boot-status --blockinfo"""

    cmdout    = \
"""Block Booting: ENABLED
"""

    stubout   = \
"""
BOOTING_STATUS

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_status_option_5():
    """
    partadm test run: boot_status_option_5
        Old Command Output:
          Block Booting: ENABLED
          

    """

    args      = """--boot-status --clean_block"""

    cmdout    = \
"""Block Booting: ENABLED
"""

    stubout   = \
"""
BOOTING_STATUS

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_status_option_6():
    """
    partadm test run: boot_status_option_6
        Old Command Output:
          Block Booting: ENABLED
          

    """

    args      = """--boot-status --recursive --blockinfo"""

    cmdout    = \
"""Block Booting: ENABLED
"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

BOOTING_STATUS

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_status_option_7():
    """
    partadm test run: boot_status_option_7
        Old Command Output:
          Block Booting: ENABLED
          

    """

    args      = """--boot-status --recursive --clean_block"""

    cmdout    = \
"""Block Booting: ENABLED
"""

    stubout   = \
"""
GET_PARTITIONS

plist: []

BOOTING_STATUS

"""

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_list_io_1():
    """
    partadm test run: list_io_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --list_io
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-G> <-E> <-T> <-_> <-I> <-O> <-_> <-B> <-L> <-O> <-C> <-K> <-S> <-
    > <-
    > <-p> <-l> <-i> <-s> <-t> <-:> <- > <-[> <-{> <-'> <-s> <-t> <-a> <-t> <-u> <-s> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-n> <-a> <-m> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-t> <-a> <-t> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-a> <-u> <-t> <-o> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-b> <-l> <-o> <-c> <-k> <-_> <-c> <-o> <-m> <-p> <-u> <-t> <-e> <-s> <-_> <-f> <-o> <-r> <-_> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-i> <-z> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-}> <-]> <-
    > 
    """

    args      = """--list_io"""

    cmdout    = \
"""Name  Size  State  CS Status  BlockComputes  Autoreboot
=========================================================
P1    0     idle   OK               x        x         
P2    1     idle   OK               x        x         
P3    2     idle   OK               x        x         
P4    3     idle   OK               x        x         
P5    4     idle   OK               x        x         
P6    5     idle   OK               x        x         
P7    6     idle   OK               x        x         
P8    7     idle   OK               x        x         
P9    8     idle   OK               x        x         
P10   9     idle   OK               x        x         
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_list_io_2():
    """
    partadm test run: list_io_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --list_io
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-G> <-E> <-T> <-_> <-I> <-O> <-_> <-B> <-L> <-O> <-C> <-K> <-S> <-
    > <-
    > <-p> <-l> <-i> <-s> <-t> <-:> <- > <-[> <-{> <-'> <-s> <-t> <-a> <-t> <-u> <-s> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-n> <-a> <-m> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-t> <-a> <-t> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-a> <-u> <-t> <-o> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-b> <-l> <-o> <-c> <-k> <-_> <-c> <-o> <-m> <-p> <-u> <-t> <-e> <-s> <-_> <-f> <-o> <-r> <-_> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-i> <-z> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-}> <-]> <-
    > 
    """

    args      = """--list_io p1 p2"""

    cmdout    = \
"""Name  Size  State  CS Status  BlockComputes  Autoreboot
=========================================================
P1    0     idle   OK               x        x         
P2    1     idle   OK               x        x         
P3    2     idle   OK               x        x         
P4    3     idle   OK               x        x         
P5    4     idle   OK               x        x         
P6    5     idle   OK               x        x         
P7    6     idle   OK               x        x         
P8    7     idle   OK               x        x         
P9    8     idle   OK               x        x         
P10   9     idle   OK               x        x         
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_list_io_3():
    """
    partadm test run: list_io_3
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: -i
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-G> <-E> <-T> <-_> <-I> <-O> <-_> <-B> <-L> <-O> <-C> <-K> <-S> <-
    > <-
    > <-p> <-l> <-i> <-s> <-t> <-:> <- > <-[> <-{> <-'> <-s> <-t> <-a> <-t> <-u> <-s> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-n> <-a> <-m> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-t> <-a> <-t> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-a> <-u> <-t> <-o> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-b> <-l> <-o> <-c> <-k> <-_> <-c> <-o> <-m> <-p> <-u> <-t> <-e> <-s> <-_> <-f> <-o> <-r> <-_> <-r> <-e> <-b> <-o> <-o> <-t> <-'> <-:> <- > <-'> <-*> <-'> <-,> <- > <-'> <-s> <-i> <-z> <-e> <-'> <-:> <- > <-'> <-*> <-'> <-}> <-]> <-
    > 
    """

    args      = """-i"""

    cmdout    = \
"""Name  Size  State  CS Status  BlockComputes  Autoreboot
=========================================================
P1    0     idle   OK               x        x         
P2    1     idle   OK               x        x         
P3    2     idle   OK               x        x         
P4    3     idle   OK               x        x         
P5    4     idle   OK               x        x         
P6    5     idle   OK               x        x         
P7    6     idle   OK               x        x         
P8    7     idle   OK               x        x         
P9    8     idle   OK               x        x         
P10   9     idle   OK               x        x         
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_add_io_block_1():
    """
    partadm test run: add_io_block_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --add_io_block
          

    """

    args      = """--add_io_block"""

    cmdout    = \
"""At least one partition must be supplied
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_add_io_block_2():
    """
    partadm test run: add_io_block_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --add_io_block
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-A> <-D> <-D> <-_> <-I> <-O> <-_> <-B> <-L> <-O> <-C> <-K> <-S> <-
    > <-
    > <-u> <-s> <-e> <-r> <- > <-n> <-a> <-m> <-e> <-:> <- > <-g> <-o> <-o> <-d> <-u> <-s> <-e> <-r> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-1> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-2> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-3> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-1> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-2> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-3> <-
    > 
    """

    args      = """--add_io_block p1 p2 p3"""

    cmdout    = \
"""['p1', 'p2', 'p3']
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_del_io_block_1():
    """
    partadm test run: del_io_block_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --del_io_block
          

    """

    args      = """--del_io_block"""

    cmdout    = \
"""At least one partition must be supplied
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_del_io_block_2():
    """
    partadm test run: del_io_block_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --del_io_block
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-D> <-E> <-L> <-_> <-I> <-O> <-_> <-B> <-L> <-O> <-C> <-K> <-S> <-
    > <-
    > <-u> <-s> <-e> <-r> <- > <-n> <-a> <-m> <-e> <-:> <- > <-g> <-o> <-o> <-d> <-u> <-s> <-e> <-r> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-1> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-2> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-3> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-1> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-2> <-
    > <-n> <-a> <-m> <-e> <-:> <-p> <-3> <-
    > 
    """

    args      = """--del_io_block p1 p2 p3"""

    cmdout    = \
"""['p1', 'p2', 'p3']
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_io_block_1():
    """
    partadm test run: boot_io_block_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --boot_io_block
          

    """

    args      = """--boot_io_block"""

    cmdout    = \
"""At least one partition must be supplied
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_boot_io_block_2():
    """
    partadm test run: boot_io_block_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --boot_io_block
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-I> <-N> <-I> <-T> <-I> <-A> <-T> <-E> <-_> <-I> <-O> <-_> <-B> <-O> <-O> <-T> <-
    > <-
    > <-w> <-h> <-o> <-a> <-m> <-i> <-:> <- > <-g> <-o> <-o> <-d> <-u> <-s> <-e> <-r> <-
    > <-t> <-a> <-g> <-:> <- > <-p> <-a> <-r> <-t> <-a> <-d> <-m> <-
    > <-p> <-a> <-r> <-t> <-s> <-:> <- > <-[> <-'> <-p> <-1> <-'> <-,> <- > <-'> <-p> <-2> <-'> <-,> <- > <-'> <-p> <-3> <-'> <-]> <-
    > 
    """

    args      = """--boot_io_block p1 p2 p3"""

    cmdout    = \
"""IO Boot initiated on p1 p2 p3
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_free_io_block_1():
    """
    partadm test run: free_io_block_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --free_io_block
          

    """

    args      = """--free_io_block"""

    cmdout    = \
"""At least one partition must be supplied
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_free_io_block_2():
    """
    partadm test run: free_io_block_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --free_io_block
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-I> <-N> <-I> <-T> <-I> <-A> <-T> <-E> <-_> <-I> <-O> <-_> <-B> <-O> <-O> <-T> <-
    > <-
    > <-w> <-h> <-o> <-a> <-m> <-i> <-:> <- > <-g> <-o> <-o> <-d> <-u> <-s> <-e> <-r> <-
    > <-f> <-o> <-r> <-c> <-e> <-:> <- > <-F> <-a> <-l> <-s> <-e> <-
    > <-p> <-a> <-r> <-t> <-s> <-:> <- > <-[> <-'> <-p> <-1> <-'> <-,> <- > <-'> <-p> <-2> <-'> <-,> <- > <-'> <-p> <-3> <-'> <-]> <-
    > 
    """

    args      = """--free_io_block p1 p2 p3"""

    cmdout    = \
"""IO Free initiated on p1 p2 p3
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_set_io_autoboot_1():
    """
    partadm test run: set_io_autoboot_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --set_io_autoboot
          

    """

    args      = """--set_io_autoboot"""

    cmdout    = \
"""At least one partition must be supplied
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_set_io_autoboot_2():
    """
    partadm test run: set_io_autoboot_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --set_io_autoboot
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-S> <-E> <-T> <-_> <-A> <-U> <-T> <-O> <-R> <-E> <-B> <-O> <-O> <-T> <-
    > <-
    > <-w> <-h> <-o> <-a> <-m> <-i> <-:> <- > <-g> <-o> <-o> <-d> <-u> <-s> <-e> <-r> <-
    > <-p> <-a> <-r> <-t> <-s> <-:> <- > <-[> <-'> <-p> <-1> <-'> <-,> <- > <-'> <-p> <-2> <-'> <-,> <- > <-'> <-p> <-3> <-'> <-]> <-
    > 
    """

    args      = """--set_io_autoboot p1 p2 p3"""

    cmdout    = \
"""Autoreboot flag set for IO Blocks: p1 p2 p3
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_unset_io_autoboot_1():
    """
    partadm test run: unset_io_autoboot_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --unset_io_autoboot
          

    """

    args      = """--unset_io_autoboot"""

    cmdout    = \
"""At least one partition must be supplied
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       256, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_unset_io_autoboot_2():
    """
    partadm test run: unset_io_autoboot_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --unset_io_autoboot
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-U> <-N> <-S> <-E> <-T> <-_> <-A> <-U> <-T> <-O> <-R> <-E> <-B> <-O> <-O> <-T> <-
    > <-
    > <-w> <-h> <-o> <-a> <-m> <-i> <-:> <- > <-g> <-o> <-o> <-d> <-u> <-s> <-e> <-r> <-
    > <-p> <-a> <-r> <-t> <-s> <-:> <- > <-[> <-'> <-p> <-1> <-'> <-,> <- > <-'> <-p> <-2> <-'> <-,> <- > <-'> <-p> <-3> <-'> <-]> <-
    > 
    """

    args      = """--unset_io_autoboot p1 p2 p3"""

    cmdout    = \
"""Autoreboot flag unset for IO Blocks: p1 p2 p3
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_io_autoboot_start_1():
    """
    partadm test run: io_autoboot_start_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --io_autoboot_start
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-E> <-N> <-A> <-B> <-L> <-E> <-_> <-I> <-O> <-_> <-A> <-U> <-T> <-O> <-R> <-E> <-B> <-O> <-O> <-T> <-
    > <-
    > 
    """

    args      = """--io_autoboot_start"""

    cmdout    = \
"""IO Block autoreboot enabled.
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_io_autoboot_start_2():
    """
    partadm test run: io_autoboot_start_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --io_autoboot_start
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-E> <-N> <-A> <-B> <-L> <-E> <-_> <-I> <-O> <-_> <-A> <-U> <-T> <-O> <-R> <-E> <-B> <-O> <-O> <-T> <-
    > <-
    > 
    """

    args      = """--io_autoboot_start p1 p2 p3"""

    cmdout    = \
"""IO Block autoreboot enabled.
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_io_autoboot_stop_1():
    """
    partadm test run: io_autoboot_stop_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --io_autoboot_stop
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-D> <-I> <-S> <-A> <-B> <-L> <-E> <-_> <-I> <-O> <-_> <-A> <-U> <-T> <-O> <-R> <-E> <-B> <-O> <-O> <-T> <-
    > <-
    > 
    """

    args      = """--io_autoboot_stop"""

    cmdout    = \
"""IO Block autoreboot disabled.
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_io_autoboot_stop_2():
    """
    partadm test run: io_autoboot_stop_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --io_autoboot_stop
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-D> <-I> <-S> <-A> <-B> <-L> <-E> <-_> <-I> <-O> <-_> <-A> <-U> <-T> <-O> <-R> <-E> <-B> <-O> <-O> <-T> <-
    > <-
    > 
    """

    args      = """--io_autoboot_stop p1 p2 p3"""

    cmdout    = \
"""IO Block autoreboot disabled.
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_io_autoboot_status_1():
    """
    partadm test run: io_autoboot_status_1
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --io_autoboot_status
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-G> <-E> <-T> <-_> <-I> <-O> <-_> <-A> <-U> <-T> <-O> <-R> <-E> <-B> <-O> <-O> <-T> <-_> <-S> <-T> <-A> <-T> <-U> <-S> <-
    > <-
    > 
    """

    args      = """--io_autoboot_status"""

    cmdout    = \
"""IO Block autoreboot: ENABLED
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result


# ---------------------------------------------------------------------------------
def test_partadm_io_autoboot_status_2():
    """
    partadm test run: io_autoboot_status_2
        Old Command Output:
          Usage: partadm.py [-a] [-d] part1 part2 (add or del)
          Usage: partadm.py -l
          Usage: partadm.py [--activate|--deactivate] part1 part2 (functional or not)
          Usage: partadm.py [--enable|--disable] part1 part2 (scheduleable or not)
          Usage: partadm.py --queue=queue1:queue2 part1 part2
          Usage: partadm.py --fail part1 part2
          Usage: partadm.py --unfail part1 part2
          Usage: partadm.py --dump
          Usage: partadm.py --xml
          Usage: partadm.py --version
          Usage: partadm.py --savestate filename
          
          Must supply one of -a or -d or -l or -start or -stop or --queue or -b
          Adding "-r" or "--recursive" will add the children of the blocks passed in.
          
          
          
          partadm.py: error: no such option: --io_autoboot_status
          
    *** STUB OUTPUT DOES NOT MATCH ***
    <-
    > <-G> <-E> <-T> <-_> <-I> <-O> <-_> <-A> <-U> <-T> <-O> <-R> <-E> <-B> <-O> <-O> <-T> <-_> <-S> <-T> <-A> <-T> <-U> <-S> <-
    > <-
    > 
    """

    args      = """--io_autoboot_status p1 p2 p3"""

    cmdout    = \
"""IO Block autoreboot: ENABLED
"""

    stubout   = ''

    stubout_file = "stub.out"

    expected_results = ( 
                       0, # Expected return status 
                       cmdout, # Expected command output
                       stubout # Expected stub functions output
                       ) 

    testutils.save_testhook("")

    results = testutils.run_cmd('partadm.py',args,stubout_file) 
    result  = testutils.validate_results(results,expected_results)

    testutils.remove_testhook()

    correct = 1
    assert result == correct, "Result:\n%s" % result

