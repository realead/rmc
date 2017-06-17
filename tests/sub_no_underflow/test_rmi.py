import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "sub01.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_two_zeros = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5"],
                                    ex.STDOUT: "0\n"} 

    casedata_2_minus_1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "2 1"],
                                    ex.STDOUT: "1\n"} 
    
    casedata_max_value_diff = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "18446744073709551615 18446744073709551614"],
                                    ex.STDOUT: "1\n"} 

    casedata_max_value_neg_diff = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "18446744073709551614 18446744073709551615"],
                                    ex.STDOUT: "0\n"} 

    casedata_sign_change = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "1 18446744073709551615"],
                                    ex.STDOUT: "0\n"} 


