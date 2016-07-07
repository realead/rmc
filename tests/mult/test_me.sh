############# SET UP ##################################
#multiplicates 1 with const 5, value in 0 und refereced by 1
PROG="mult"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "0" 
check_prog_output "2 1 0" "5"   
check_prog_output "3 2 1 0" "10"  
check_prog_output "3 3689348814741910323 1" "18446744073709551615" max_val
check_prog_output "3 3689348814741910323 2 9223372036854775808" "9223372036854775808" overflow


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

