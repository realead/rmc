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
only_compile "end/operand_for_end"  "no operand for END expected, but found 34"

########### CLEAN UP #################################################

rm *.s

############ REPORT ################################################## 
report

exit $failed_cnt


