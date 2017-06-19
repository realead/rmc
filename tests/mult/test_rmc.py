import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "mult"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_0 = {ex.OPTIONS: ["5"],
                                    ex.STDOUT: "0\n"} 

    casedata_5 = {ex.OPTIONS: ["2", "1", "0"],
                                    ex.STDOUT: "5\n"} 
    
    casedata_10= {ex.OPTIONS: ["3", "2", "1", "0"],
                                    ex.STDOUT: "10\n"} 

    casedata_maxval= {ex.OPTIONS: ["3", "3689348814741910323", "1"],
                                    ex.STDOUT: "18446744073709551615\n"}  

    casedata_overflow = {ex.OPTIONS: ["3", "3689348814741910323", "2", "9223372036854775808"],
                                    ex.STDOUT: "9223372036854775808\n"}

