import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "add.rm")]


@dec.to_unit_tests
class AddInterpreterTester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_5plus0plus0 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5"],
                            ex.STDOUT: "5\n"} 

    casedata_5plus1plus1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "1 0"],
                            ex.STDOUT: "7\n"} 

    casedata_5plus2plus1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "2 1 0"],
                            ex.STDOUT: "8\n"}     

    casedata_max_value = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "18446744073709551610 2 0"],
                            ex.STDOUT: "18446744073709551615\n"}


    casedata_overflow = {   
                            ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "18446744073709551610 1"],
                            ex.STDOUT: "0\n"}


