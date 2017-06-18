import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "add"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}


    casedata_5plus0plus0 = {ex.OPTIONS: ["5"],
                             ex.STDOUT: "5\n"} 

    casedata_5plus1plus1 = {ex.OPTIONS: ["2", "1", "0"],
                            ex.STDOUT: "7\n"} 

    casedata_5plus2plus1 = {ex.OPTIONS: ["3", "2", "1", "0"],
                            ex.STDOUT: "8\n"}     

    casedata_max_value = {ex.OPTIONS: ["3", "18446744073709551610", "2", "0"],
                            ex.STDOUT: "18446744073709551615\n"}


    casedata_overflow = {ex.OPTIONS: ["3", "18446744073709551610", "1"],
                            ex.STDOUT: "0\n"}


