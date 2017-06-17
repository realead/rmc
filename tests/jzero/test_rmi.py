import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "jzero.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_takesecond = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "1 5 6"],
                                    ex.STDOUT: "6\n"} 

    casedata_takesecond2 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "2 5 6"],
                                    ex.STDOUT: "6\n"} 

    casedata_takefirst = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "0 5 6"],
                                    ex.STDOUT: "5\n"}  

