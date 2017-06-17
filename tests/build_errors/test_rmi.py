import os

import exetest as ex
import exetest.decorator as dec



COMMON_OPTIONS = [os.environ["RMI"],"-n", "100", "-f"]
MY_PATH = os.path.dirname(__file__)



def create_casedata(file_name, error_message, error_line_number=1):
    file_name=os.path.join(MY_PATH, file_name+".rm")
    line_report = "" if error_line_number is None else " in line {0}".format(error_line_number)
    return {ex.OPTIONS: COMMON_OPTIONS +  [file_name],
                              ex.STDERR: "error compiling {0}{1}: {2}\n".format(file_name, line_report, error_message)} 


@dec.to_unit_tests
class MiscTester: 
    exe="python"
    default_parameters = {ex.EXIT_CODE: 1,
                          ex.STDOUT: "",
                          ex.INPUT: ""}
    
    casedata_missing_instr = create_casedata("missing_instruction", "operation expected, but none found", 2) 
    casedata_unknown_instr = create_casedata("unknown_instruction", "unknown instruction STRE") 

    casedata_neg_b = create_casedata("b/neg_b","b must be a positive integer, found -1")
    casedata_no_b = create_casedata("b/no_b","b must be a positive integer, found STORE")
    casedata_non_continious_b = create_casedata("b/non_continious_b","expected b is 2, found b is 3", 2)
    casedata_null_b = create_casedata("b/null_b","b must be a positive integer, found 0")
    casedata_wrong_b_start = create_casedata("b/wrong_b_start","expected b is 1, found b is 2")


    casedata_end_empty = create_casedata( "end/empty","exact one END instruction expected, but 0 found", None)
    casedata_end_no_end = create_casedata( "end/no_end","exact one END instruction expected, but 0 found", None)
    casedata_end_two_ends = create_casedata( "end/two_ends","exact one END instruction expected, but 2 found", None)
    casedata_end_operand_for_end = create_casedata( "end/operand_for_end","END does not expect operands but 1 found", 1)
 



