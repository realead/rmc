############# SET UP ##################################
#finds the max of n numbers (last number of the series must be 0)
#register 0 and 1 are for variables, numbers start in register 2
PROG="max"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "2" "0"  both_nulls
check_prog_output "2 1 1" "1"  only_1s 
check_prog_output "2 5 1" "5" max_first
check_prog_output "2 5 6" "6" max_second


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

