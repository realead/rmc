import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMJIT"], "-f", os.path.join(os.path.dirname(__file__), "max.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_both_nulls = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "0 0"],
                                    ex.STDOUT: "0\n"} 

    casedata_both_ones = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "1 1"],
                                    ex.STDOUT: "1\n"} 

    casedata_max_first= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "5 1"],
                                    ex.STDOUT: "5\n"}  

    casedata_max_second = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "5 6"],
                                    ex.STDOUT: "6\n"}


