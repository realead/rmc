import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "move2_to_0.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5"],
                                    ex.STDOUT: "0\n"} 

    casedata_2 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "1 0 33"],
                                    ex.STDOUT: "33\n"} 

    casedata_3= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "23", "-i", "235 11 0 333 44"],
                                    ex.STDOUT: "0\n"}  

    casedata_4 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "23", "-i", "0 11 15 333 44"],
                                    ex.STDOUT: "15\n"}


