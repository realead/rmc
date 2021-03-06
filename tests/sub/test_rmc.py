import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "sub"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_1 = {ex.OPTIONS: ["5"],
                                    ex.STDOUT: "95\n"} 

    casedata_2 = {ex.OPTIONS: ["2", "1", "0"],
                                    ex.STDOUT: "93\n"} 
    
    casedata_3 = {ex.OPTIONS: ["3", "2", "1", "0"],
                                    ex.STDOUT: "92\n"}  

