import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "dummy_test.rm")]


@dec.to_unit_tests
class Tester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: "",
                          ex.STDOUT: ""}
    
    casedata_0 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5", "-i", "0"],
                             ex.STDOUT: "0\n"} 

    casedata_1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "1", "-i", "1"],
                            ex.STDOUT: "1\n"} 

    casedata_235 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "23", "-i", "235"],
                            ex.STDOUT: "235\n"}     


    #star_up errors
    casedata_not_a_number  = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "1.4", "-i", "1"], ex.EXIT_CODE: 2}

    casedata_not_a_number2 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "1.4"], ex.EXIT_CODE: 2}
   
    casedata_neg_regs = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "-1"], ex.EXIT_CODE: 2}

    casedata_zero_regs = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "0"], ex.EXIT_CODE: 5}

    casedata_no_arguments = {ex.OPTIONS: COMMON_OPTIONS + [], ex.EXIT_CODE: 4}

    casedata_more_i_than_n = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "1", "-i", "4 5"], ex.EXIT_CODE: 6}


