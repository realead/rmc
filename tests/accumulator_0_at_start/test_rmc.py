import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "accumulator_0_at_start"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: "",
                          ex.STDOUT: "0\n"}
    
    casedata_nothing_initialized = {ex.OPTIONS: ["4"]} 

    casedata_5plus1plus1initialized_with_1 = {ex.OPTIONS: ["1", "1"]} 

    casedata_initialized_with_235 = {ex.OPTIONS: ["3", "235", "22", "22"]}  

