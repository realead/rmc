import os
import exetest as ex
import exetest.decorator as dec

import RMCTester



@dec.to_unit_tests
class Tester(RMCTester.RMCTester): 

    #setting up the test case
    my_path = os.path.dirname(__file__)
    program_name = "dummy_test"

    exe = os.path.join(my_path, RMCTester.RMCTester.EXE_NAME)

    
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: "",
                          ex.STDOUT: ""}


    casedata_0 = {ex.OPTIONS: ["5", "0"],
                             ex.STDOUT: "0\n"} 

    casedata_1 = {ex.OPTIONS: ["1", "1"],
                            ex.STDOUT: "1\n"} 

    casedata_235 = {ex.OPTIONS: ["23", "235"],
                            ex.STDOUT: "235\n"}     


    #star_up errors
    casedata_not_a_number  = {ex.OPTIONS: ["1.4", "1"], ex.EXIT_CODE: 2}

    casedata_not_a_number2 = {ex.OPTIONS: ["3", "1.4"], ex.EXIT_CODE: 2}
   
    casedata_neg_regs = {ex.OPTIONS: ["-1"], ex.EXIT_CODE: 2}

    casedata_zero_regs = {ex.OPTIONS: ["0"], ex.EXIT_CODE: 5}

    casedata_no_arguments = {ex.OPTIONS: [], ex.EXIT_CODE: 4}

    casedata_more_i_than_n = {ex.OPTIONS: ["1", "4", "5"], ex.EXIT_CODE: 6}


