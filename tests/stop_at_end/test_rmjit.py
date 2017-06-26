import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMJIT"], "-f", os.path.join(os.path.dirname(__file__), "stop_at_end.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5"],
                                    ex.STDOUT: "0\n"} 

    casedata_2 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "1", "-i", "0"],
                                    ex.STDOUT: "0\n"} 
    
    casedata_3 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "22", "-i", "235 44"],
                                    ex.STDOUT: "235\n"} 


