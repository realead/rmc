############# SET UP ################################################
#load functions:

. $TOOLS/utils.sh

############### COMPILE ##############################################

only_compile "unknown_instruction"  "unknown instruction STRE"
only_compile "neg_b"                "b must be a positive integer, found -1"
only_compile "no_b"                 "b must be a positive integer, found STORE"
only_compile "non_continious_b"
only_compile "null_b"               "b must be a positive integer, found 0"
only_compile "wrong_b_start"



########### CLEAN UP #################################################

rm *.s

############ REPORT ################################################## 
report

exit $failed_cnt


