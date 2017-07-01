import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "last_goto"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_0 = {ex.OPTIONS: ["5"],
                                    ex.STDOUT: "0\n"} 

    casedata_1 = {ex.OPTIONS: ["1", "5"],
                                    ex.STDOUT: "5\n"} 

    casedata_2 = {ex.OPTIONS: ["22", "24"],
                                    ex.STDOUT: "24\n"}  

