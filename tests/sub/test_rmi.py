import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "sub.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5"],
                                    ex.STDOUT: "95\n"} 

    casedata_2 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "1 0"],
                                    ex.STDOUT: "93\n"} 
    
    casedata_3 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "2 1 0"],
                                    ex.STDOUT: "92\n"} 


