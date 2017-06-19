import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "find_max"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_no_elements= {ex.OPTIONS: ["3", "0", "0", "0"],
                                    ex.STDOUT: "0\n"} 

    casedata_only1 = {ex.OPTIONS: ["10", "0", "0", "1"],
                                    ex.STDOUT: "1\n"} 

    casedata_only1b = {ex.OPTIONS: ["10", "1000", "1000", "1"],
                                    ex.STDOUT: "1\n"}  

    casedata_1_til_7 = {ex.OPTIONS: ["10", "3000", "4000", "1", "2", "3", "4", "5", "6", "7"],
                                    ex.STDOUT: "7\n"} 

    casedata_random = {ex.OPTIONS: ["20", "0", "0", "3", "56", "83", "12", "9", "66", "2", "7777", "32", "2222"],
                                    ex.STDOUT: "7777\n"} 

