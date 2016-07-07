############# SET UP ##################################
#calculates diff between values in 0 and 1
PROG="sub01"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "0" two_zeros 
check_prog_output "2 2 1" "1" 2_minus_1   
check_prog_output "2 1 2" "0" 1_minus_1
check_prog_output "2 18446744073709551615 18446744073709551614"  "1" max_value_diff
check_prog_output "2 18446744073709551614 18446744073709551615"  "0" max_value_neg_diff
check_prog_output "2 1 18446744073709551615"  "0" sign_change


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

