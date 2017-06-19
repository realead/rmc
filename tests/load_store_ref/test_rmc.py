import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "load_store_ref"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_case1 = {ex.OPTIONS: ["5", "1", "2"],
                                    ex.STDOUT: "2\n"} 

    casedata_goal_is_0 = {ex.OPTIONS: ["2", "0", "0"],
                                    ex.STDOUT: "0\n"} 

    casedata_goal_is_last_reg = {ex.OPTIONS: ["23", "2", "22", "444"],
                                    ex.STDOUT: "444\n"}  

