############# SET UP ################################################
#load functions:

. $TOOLS/utils.sh

############### COMPILE ##############################################

only_compile "unknown_instruction"  "unknown instruction STRE"
only_compile "missing_instruction"  "operation expected, but none found"

only_compile "b/neg_b"                "b must be a positive integer, found -1"
only_compile "b/no_b"                 "b must be a positive integer, found STORE"
only_compile "b/non_continious_b"     "expected b is 2, found b is 3"
only_compile "b/null_b"               "b must be a positive integer, found 0"
only_compile "b/wrong_b_start"        "expected b is 1, found b is 2"

only_compile "end/empty"            "exact one END instruction expected, but 0 found"
only_compile "end/no_end"           "exact one END instruction expected, but 0 found"
only_compile "end/two_ends"         "exact one END instruction expected, but 2 found"
only_compile "end/operand_for_end"  "END does not expect operands but 1 found"


only_compile "wrong_int/neg_index"              "index must be a nonnegative integer, found -1"
only_compile "wrong_int/neg_ref"                "index must be a nonnegative integer, found -1"
only_compile "wrong_int/neg_const"              "constant must be a nonnegative integer, found -1"

only_compile "wrong_int/nonnum_index"           "index must be a nonnegative integer, found 12A"
only_compile "wrong_int/nonnum_ref"           "index must be a nonnegative integer, found 12A"
only_compile "wrong_int/nonnum_const"           "constant must be a nonnegative integer, found 1.2"

only_compile "wrong_int/plus_index"             "index must be a nonnegative integer, found +1"
only_compile "wrong_int/plus_ref"             "index must be a nonnegative integer, found +1"
only_compile "wrong_int/plus_const"             "constant must be a nonnegative integer, found +1"

only_compile "STORE/no_operands"                "STORE expects exact 1 operand but 0 found"
only_compile "STORE/store2const"                "cannot store into a constant, need register or register reference"
only_compile "STORE/two_operands"               "STORE expects exact 1 operand but 2 found"

only_compile "LOAD/no_operands"                "LOAD expects exact 1 operand but 0 found"
only_compile "LOAD/two_operands"               "LOAD expects exact 1 operand but 2 found"

only_compile "ADD/no_operands"                "ADD expects exact 1 operand but 0 found"
only_compile "ADD/two_operands"               "ADD expects exact 1 operand but 2 found"

only_compile "MULT/no_operands"                "MULT expects exact 1 operand but 0 found"
only_compile "MULT/two_operands"               "MULT expects exact 1 operand but 2 found"

only_compile "SUB/no_operands"                "SUB expects exact 1 operand but 0 found"
only_compile "SUB/two_operands"               "SUB expects exact 1 operand but 2 found"

only_compile "DIV/no_operands"                "DIV expects exact 1 operand but 0 found"
only_compile "DIV/two_operands"               "DIV expects exact 1 operand but 2 found"


only_compile "GOTO/no_operands"                 "GOTO expects exact 1 operand but 0 found"
only_compile "GOTO/two_operands"                "GOTO expects exact 1 operand but 2 found"
only_compile "GOTO/goto0"                       "GOTO label must positive, but is 0"
only_compile "GOTO/goto_index"                  "GOTO label must be a const, but is 0"
only_compile "GOTO/goto_ref"                    "GOTO label must be a const, but is *0"
only_compile "GOTO/unknown_label"               "unknown GOTO label 100, there are only 2 lines"

########### CLEAN UP #################################################

if [ "$1" != "--keep" ]; then
    rm *.s
    #clean up in subdirs:
    for dir in *
    do
        if [ -d $dir ]; then
            cd $dir
            rm *.s
            cd ..
        fi
    done
fi

############ REPORT ################################################## 
report

exit $failed_cnt


