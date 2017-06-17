import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "mult.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_0 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5"],
                                    ex.STDOUT: "0\n"} 

    casedata_5 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "1 0"],
                                    ex.STDOUT: "5\n"} 
    
    casedata_10= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "2 1 0"],
                                    ex.STDOUT: "10\n"} 

    casedata_maxval= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "3689348814741910323 1"],
                                    ex.STDOUT: "18446744073709551615\n"}  

    casedata_overflow = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "3689348814741910323 2 9223372036854775808"],
                                    ex.STDOUT: "9223372036854775808\n"}

