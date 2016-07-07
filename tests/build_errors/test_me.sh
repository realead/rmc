############# SET UP ################################################
#load functions:

. $TOOLS/utils.sh

############### COMPILE ##############################################

only_compile "unknown_instruction"  "unknown instruction STRE"
only_compile "neg_b"                "b must be a positive integer, found -1"
only_compile "no_b"                 "b must be a positive integer, found STORE"
only_compile "non_continious_b"     "expected b is 2, found b is 3"
only_compile "null_b"               "b must be a positive integer, found 0"
only_compile "wrong_b_start"        "expected b is 1, found b is 2"

only_compile "end/empty"            "exact one END instruction expected, but 0 found"
only_compile "end/no_end"           "exact one END instruction expected, but 0 found"
only_compile "end/two_ends"         "exact one END instruction expected, but 2 found"
only_compile "end/operand_for_end"  "END does not expect operands but 1 found"


only_compile "wrong_int/neg_index"              "index must be a nonnegative integer, found -1"
only_compile "wrong_int/nonnum_index"           "index must be a nonnegative integer, found 12A"
only_compile "wrong_int/plus_index"             "index must be a nonnegative integer, found +1"

only_compile "STORE/no_operands"                "STORE expects exact 1 operand but 0 found"
only_compile "STORE/store2const"                "cannot store into a constant, need register or register reference"
only_compile "STORE/two_operands"               "STORE expects exact 1 operand but 2 found"

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


