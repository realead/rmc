import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "power"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_0p0 = {ex.OPTIONS: ["3", "0", "0", "0"],
                                    ex.STDOUT: "1\n"} 

    casedata_5p0 = {ex.OPTIONS: ["3", "5", "0"],
                                    ex.STDOUT: "1\n"} 
    
    casedata_overflow= {ex.OPTIONS: ["3", "2", "64", "444"],
                                    ex.STDOUT: "0\n"} 

    casedata_5p4= {ex.OPTIONS: ["3", "5", "4"],
                                    ex.STDOUT: "625\n"}  

    casedata_2p63 = {ex.OPTIONS: ["3", "2", "63"],
                                    ex.STDOUT: "9223372036854775808\n"}

