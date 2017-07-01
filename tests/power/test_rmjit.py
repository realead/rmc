import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMJIT"], "-f", os.path.join(os.path.dirname(__file__), "power.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_0p0 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "0 0 0"],
                                    ex.STDOUT: "1\n"} 

    casedata_5p0 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "5 0"],
                                    ex.STDOUT: "1\n"} 
    
    casedata_overflow= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "2 64 444"],
                                    ex.STDOUT: "0\n"} 

    casedata_5p4= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "5 4"],
                                    ex.STDOUT: "625\n"}  

    casedata_2p63 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "2 63"],
                                    ex.STDOUT: "9223372036854775808\n"}

