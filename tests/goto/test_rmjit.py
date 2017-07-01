import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMJIT"], "-f", os.path.join(os.path.dirname(__file__), "goto.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: "",
                          ex.STDOUT: "0\n"}
    
    casedata_0 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5"],
                                    ex.STDOUT: "100\n"} 

    casedata_1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "1", "-i", "1"],
                                    ex.STDOUT: "96\n"} 

    casedata_24 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "1", "-i", "24"],
                                    ex.STDOUT: "4\n"}  

    casedata_exact = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "1", "-i", "25"],
                                    ex.STDOUT: "0\n"} 

    casedata_overflow = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "26"],
                                    ex.STDOUT: "0\n"} 
