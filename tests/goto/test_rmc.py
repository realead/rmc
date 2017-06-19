import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "goto"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_0 = {ex.OPTIONS: ["5"],
                                    ex.STDOUT: "100\n"} 

    casedata_1 = {ex.OPTIONS: ["1", "1"],
                                    ex.STDOUT: "96\n"} 

    casedata_24 = {ex.OPTIONS: ["1", "24"],
                                    ex.STDOUT: "4\n"}  

    casedata_exact = {ex.OPTIONS: ["1", "25"],
                                    ex.STDOUT: "0\n"} 

    casedata_overflow = {ex.OPTIONS: ["3", "26"],
                                    ex.STDOUT: "0\n"} 

