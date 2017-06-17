import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "factorial.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: "",
                          ex.STDOUT: "0\n"}
    
    casedata_factorial0= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "0 0"],
                                    ex.STDOUT: "1\n"} 

    casedata_factorial1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "1 0"],
                                    ex.STDOUT: "1\n"} 

    casedata_factorial2 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "2 64"],
                                    ex.STDOUT: "2\n"}  

    casedata_factorial3= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "3 4"],
                                    ex.STDOUT: "6\n"} 

    casedata_factorial4 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "4 64"],
                                    ex.STDOUT: "24\n"} 

    casedata_factorial5 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "5"],
                                    ex.STDOUT: "120\n"}   



