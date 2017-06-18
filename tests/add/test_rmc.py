import os
import errno

import exetest as ex
import exetest.decorator as dec
import exetest.executor as exe


MY_PATH = os.path.dirname(__file__)
MY_PROGRAM = os.path.join(MY_PATH, "add.rm")
MY_EXE = os.path.join(MY_PATH, "my_exe")


def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

@dec.to_unit_tests
class Tester: 
    exe=MY_EXE

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}

    def setUp(self):
        #remove old data, if needed:
        silent_remove(MY_EXE)
        silent_remove(os.path.join(MY_PATH, "add.o"))
        silent_remove(os.path.join(MY_PATH, "add.s"))

        
        build_pars={ex.EXIT_CODE: 0, 
                    ex.OPTIONS: [os.environ["RMC"], "-c", MY_PROGRAM, "-o", MY_EXE]}
        res, msg = exe.execute("python", build_pars)
        self.assertTrue(res, msg="Could not set up: "+msg)

    def tearDown(self):#kind of the check, that the build-step delivered it right
        os.remove(MY_EXE)
        os.remove(os.path.join(MY_PATH, "add.o"))
        os.remove(os.path.join(MY_PATH, "atouq.o"))
        os.remove(os.path.join(MY_PATH, "print_newline.o"))
        os.remove(os.path.join(MY_PATH, "startup.o"))
        os.remove(os.path.join(MY_PATH, "error_exit.o"))
        os.remove(os.path.join(MY_PATH, "uqtoa.o"))
        os.remove(os.path.join(MY_PATH, "add.s"))


    casedata_5plus0plus0 = {ex.OPTIONS: ["5"],
                             ex.STDOUT: "5\n"} 

    casedata_5plus1plus1 = {ex.OPTIONS: ["2", "1", "0"],
                            ex.STDOUT: "7\n"} 

    casedata_5plus2plus1 = {ex.OPTIONS: ["3", "2", "1", "0"],
                            ex.STDOUT: "8\n"}     

    casedata_max_value = {ex.OPTIONS: ["3", "18446744073709551610", "2", "0"],
                            ex.STDOUT: "18446744073709551615\n"}


    casedata_overflow = {ex.OPTIONS: ["3", "18446744073709551610", "1"],
                            ex.STDOUT: "0\n"}


