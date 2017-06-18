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

    casedata_int_neg_index = create_casedata("wrong_int/neg_index","index must be a nonnegative integer, found -1")
    casedata_int_neg_ref = create_casedata("wrong_int/neg_ref","index must be a nonnegative integer, found -1")
    casedata_int_neg_const= create_casedata("wrong_int/neg_const","constant must be a nonnegative integer, found -1")

    casedata_int_nonnumindex= create_casedata("wrong_int/nonnum_index","index must be a nonnegative integer, found 12A")
    casedata_int_nonnumref= create_casedata("wrong_int/nonnum_ref","index must be a nonnegative integer, found 12A" )
    casedata_int_nononumconst= create_casedata("wrong_int/nonnum_const","constant must be a nonnegative integer, found 1.2")

    casedata_int_plusindex= create_casedata("wrong_int/plus_index","index must be a nonnegative integer, found +1")
    casedata_int_plusref= create_casedata("wrong_int/plus_ref", "index must be a nonnegative integer, found +1")
    casedata_int_plusconst= create_casedata("wrong_int/plus_const","constant must be a nonnegative integer, found +1")


    casedata_store_no_operands= create_casedata("STORE/no_operands", "STORE expects exact 1 operand but 0 found")
    casedata_store_to_const= create_casedata("STORE/store2const", "cannot store into a constant, need register or register reference")
    casedata_store_two_operands= create_casedata("STORE/two_operands", "STORE expects exact 1 operand but 2 found")

    casedata_load_no_operands= create_casedata("LOAD/no_operands","LOAD expects exact 1 operand but 0 found")
    casedata_load_two_operands= create_casedata("LOAD/two_operands","LOAD expects exact 1 operand but 2 found")

    casedata_add_no_operands= create_casedata("ADD/no_operands","ADD expects exact 1 operand but 0 found")
    casedata_add_two_operands= create_casedata("ADD/two_operands","ADD expects exact 1 operand but 2 found")

    casedata_mult_no_operands= create_casedata("MULT/no_operands","MULT expects exact 1 operand but 0 found")
    casedata_mult_two_operands= create_casedata("MULT/two_operands","MULT expects exact 1 operand but 2 found")

    casedata_sub_no_operands= create_casedata("SUB/no_operands","SUB expects exact 1 operand but 0 found")
    casedata_sub_two_operands= create_casedata("SUB/two_operands","SUB expects exact 1 operand but 2 found")

    casedata_div_no_operands= create_casedata("DIV/no_operands", "DIV expects exact 1 operand but 0 found")
    casedata_div_two_operands= create_casedata("DIV/two_operands","DIV expects exact 1 operand but 2 found")


    casedata_goto_no_operands= create_casedata("GOTO/no_operands","GOTO expects exact 1 operand but 0 found")
    casedata_goto_two_operands= create_casedata("GOTO/two_operands","GOTO expects exact 1 operand but 2 found")
    casedata_goto_goto0= create_casedata("GOTO/goto0","GOTO label must positive, but is 0")
    casedata_goto_index= create_casedata("GOTO/goto_index","GOTO label must be a const, but is 0")
    casedata_goto_gotoref= create_casedata("GOTO/goto_ref","GOTO label must be a const, but is *0")
    casedata_goto_unknown_label= create_casedata("GOTO/unknown_label","unknown GOTO/JZERO label 100, there are only 2 lines", None)


    casedata_jzero_no_operands= create_casedata("JZERO/no_operands","JZERO expects exact 1 operand but 0 found")
    casedata_jzero_two_operands= create_casedata("JZERO/two_operands","JZERO expects exact 1 operand but 2 found")
    casedata_jzero_jzero0= create_casedata("JZERO/jzero0","JZERO label must positive, but is 0")
    casedata_jzero_index= create_casedata("JZERO/jzero_index","JZERO label must be a const, but is 0")
    casedata_jzero_ref= create_casedata("JZERO/jzero_ref","JZERO label must be a const, but is *0")
    casedata_jzero_unknown_label= create_casedata("JZERO/unknown_label","unknown GOTO/JZERO label 100, there are only 2 lines", None)
 



