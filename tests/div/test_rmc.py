import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "div"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_div1= {ex.OPTIONS: ["5", "1", "0"],
                    ex.STDOUT: "24\n"} 

    casedata_div2 = {ex.OPTIONS: ["2", "4", "1"],
                     ex.STDOUT: "6\n"} 

    casedata_div3 = {ex.OPTIONS: ["3", "1", "2", "7"],
                     ex.STDOUT: "3\n"}  

