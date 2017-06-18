import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"], "-f", os.path.join(os.path.dirname(__file__), "accumulator_0_at_start.rm")]


@dec.to_unit_tests
class RMITester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 0,
                          ex.STDERR: "",
                          ex.INPUT: "",
                          ex.STDOUT: "0\n"}
    
    casedata_nothing_initialized = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "4",]} 

    casedata_5plus1plus1initialized_with_1 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "1", "-i", "1"]} 

    casedata_initialized_with_235 = {ex.OPTIONS: COMMON_OPTIONS + ["-n", "3", "-i", "235 22 22"]}     



