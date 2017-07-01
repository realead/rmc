import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMJIT"], "-f", os.path.join(os.path.dirname(__file__), "near_jumps.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_jzero = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "0 120"],
                                    ex.STDOUT: "86\n"} 

    casedata_jmp = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "1 120"],
                                    ex.STDOUT: "85\n"} 

