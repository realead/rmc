import os
import errno

import exetest as ex
import exetest.executor as exe



def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred


class RMCTester:
    #needed properties: 
    #my_path
    #program_name
    EXE_NAME =  "prog"

    def setUp(self):
        #remove old data, if needed:
        prog = os.path.join(self.my_path, self.EXE_NAME)
        rm = os.path.join(self.my_path, self.program_name+".rm")
        silent_remove(prog)
        silent_remove(os.path.join(self.my_path, self.program_name+".o"))
        silent_remove(os.path.join(self.my_path, self.program_name+".s"))
        build_pars={ex.EXIT_CODE: 0, ex.STDERR: "", ex.INPUT: "", ex.STDOUT: "", 
                    ex.OPTIONS: [os.environ["RMC"], "-c", rm, "-o", prog]}
        res, msg = exe.execute("python", build_pars)
        self.assertTrue(res, msg="Could not set up: "+msg)



    def tearDown(self):#kind of the check, that the build-step delivered it right
        try:
            keep_temps = os.environ["KEEP"]
        except:
            keep_temps = "NO"

        if keep_temps != "YES":
            os.remove(os.path.join(self.my_path, self.EXE_NAME))
            os.remove(os.path.join(self.my_path, self.program_name+".o"))
            os.remove(os.path.join(self.my_path, self.program_name+".s"))
            os.remove(os.path.join(self.my_path, "atouq.o"))
            os.remove(os.path.join(self.my_path, "print_newline.o"))
            os.remove(os.path.join(self.my_path, "startup.o"))
            os.remove(os.path.join(self.my_path, "error_exit.o"))
            os.remove(os.path.join(self.my_path, "uqtoa.o"))





