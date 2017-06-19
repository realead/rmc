import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "factorial"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_factorial0= {ex.OPTIONS: [ "2", "0", "0"],
                                    ex.STDOUT: "1\n"} 

    casedata_factorial1 = {ex.OPTIONS: ["2", "1", "0"],
                                    ex.STDOUT: "1\n"} 

    casedata_factorial2 = {ex.OPTIONS: ["2", "2", "64"],
                                    ex.STDOUT: "2\n"}  

    casedata_factorial3= {ex.OPTIONS: ["2", "3", "4"],
                                    ex.STDOUT: "6\n"} 

    casedata_factorial4 = {ex.OPTIONS: [ "2", "4", "64"],
                                    ex.STDOUT: "24\n"} 

    casedata_factorial5 = {ex.OPTIONS:  [ "2", "5"],
                                    ex.STDOUT: "120\n"}

