import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "load_store_ref.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: ""}
    
    casedata_case1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "5", "-i", "1 2"],
                                    ex.STDOUT: "2\n"} 

    casedata_goal_is_0 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "2", "-i", "0 0"],
                                    ex.STDOUT: "0\n"} 

    casedata_goal_is_last_reg = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "23", "-i", "2 22 444"],
                                    ex.STDOUT: "444\n"}  

