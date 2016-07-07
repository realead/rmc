############# SET UP ##################################
#adds const 5, value in 0 und refereced by 1
PROG="add"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "5" 
check_prog_output "2 1 0" "7"   
check_prog_output "3 2 1 0" "8"  
check_prog_output "3 18446744073709551610 2 0" "18446744073709551615" max_val
check_prog_output "2 18446744073709551610 1" "0" overflow


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

