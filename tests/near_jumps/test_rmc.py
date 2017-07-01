import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "near_jumps"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_jzero = {ex.OPTIONS: ["2", "0", "120"],
                                    ex.STDOUT: "86\n"} 

    casedata_jmp = {ex.OPTIONS: ["2", "1", "120"],
                                    ex.STDOUT: "85\n"} 
 

