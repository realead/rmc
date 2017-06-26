import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMJIT"], "-f", os.path.join(os.path.dirname(__file__), "div.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: "",
                          ex.STDOUT: "0\n"}
    
    casedata_div1= {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5", "-i", "1 0"],
                                    ex.STDOUT: "24\n"} 

    casedata_div2 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "4 1"],
                                    ex.STDOUT: "6\n"} 

    casedata_div3 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "1 2 7"],
                                    ex.STDOUT: "3\n"}    

 



