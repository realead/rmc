import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "jzero"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_takesecond = {ex.OPTIONS: ["3", "1", "5", "6"],
                                    ex.STDOUT: "6\n"} 

    casedata_takesecond2 = {ex.OPTIONS: ["3", "2", "5", "6"],
                                    ex.STDOUT: "6\n"} 

    casedata_takefirst = {ex.OPTIONS: ["3", "0", "5", "6"],
                                    ex.STDOUT: "5\n"}  

