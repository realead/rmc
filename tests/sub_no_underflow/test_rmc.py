import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "sub01"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_two_zeros = {ex.OPTIONS: ["5"],
                                    ex.STDOUT: "0\n"} 

    casedata_2_minus_1 = {ex.OPTIONS: ["2", "2", "1"],
                                    ex.STDOUT: "1\n"} 
    
    casedata_max_value_diff = {ex.OPTIONS: ["2", "18446744073709551615", "18446744073709551614"],
                                    ex.STDOUT: "1\n"} 

    casedata_max_value_neg_diff = {ex.OPTIONS: ["2", "18446744073709551614", "18446744073709551615"],
                                    ex.STDOUT: "0\n"} 

    casedata_sign_change = {ex.OPTIONS: ["2", "1", "18446744073709551615"],
                                    ex.STDOUT: "0\n"}  

