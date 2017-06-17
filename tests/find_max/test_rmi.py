import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "find_max.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: "",
                          ex.STDOUT: "0\n"}
    
    casedata_no_elements= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "0 0 0"],
                                    ex.STDOUT: "0\n"} 

    casedata_only1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "10", "-i", "0 0 1"],
                                    ex.STDOUT: "1\n"} 

    casedata_only1b = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "10", "-i", "1000 1000 1"],
                                    ex.STDOUT: "1\n"}  

    casedata_1_til_7 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "10", "-i", "3000 4000 1 2 3 4 5 6 7"],
                                    ex.STDOUT: "7\n"} 

    casedata_random = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "20", "-i", "0 0 3 56 83 12 9 66 2 7777 32 2222"],
                                    ex.STDOUT: "7777\n"} 
 


