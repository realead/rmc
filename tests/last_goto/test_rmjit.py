import os

import exetest as ex
import exetest.decorator as dec




COMMON_OPTIONS = [os.environ["RMJIT"], "-f", os.path.join(os.path.dirname(__file__), "last_goto.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_0 = {ex.OPTIONS: COMMON_OPTIONS+["-n", "5"],
                  ex.STDOUT: "0\n"} 

    casedata_1 = {ex.OPTIONS: COMMON_OPTIONS+["-n", "1", "-i", "5"],
                  ex.STDOUT: "5\n"} 

    casedata_2 = {ex.OPTIONS: COMMON_OPTIONS+["-n", "22", "-i", "24"],
                  ex.STDOUT: "24\n"} 
