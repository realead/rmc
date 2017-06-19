import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "max"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_both_nulls = {ex.OPTIONS: ["2", "0", "0"],
                                    ex.STDOUT: "0\n"} 

    casedata_both_ones = {ex.OPTIONS: ["2", "1", "1"],
                                    ex.STDOUT: "1\n"} 

    casedata_max_first= {ex.OPTIONS: ["2", "5", "1"],
                                    ex.STDOUT: "5\n"}  

    casedata_max_second = {ex.OPTIONS: ["2", "5", "6"],
                                    ex.STDOUT: "6\n"} 

