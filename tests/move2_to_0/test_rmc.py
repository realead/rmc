import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "move2_to_0"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_1 = {ex.OPTIONS: ["5"],
                                    ex.STDOUT: "0\n"} 

    casedata_2 = {ex.OPTIONS: ["3", "1", "0", "33"],
                                    ex.STDOUT: "33\n"} 

    casedata_3= {ex.OPTIONS: ["23", "235", "11", "0", "333", "44"],
                                    ex.STDOUT: "0\n"}  

    casedata_4 = {ex.OPTIONS: ["23", "0", "11", "15", "333", "44"],
                                    ex.STDOUT: "15\n"}

