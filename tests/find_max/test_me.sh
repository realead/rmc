############# SET UP ##################################
#finds the max of n numbers (last number of the series must be 0)
#register 0 and 1 are for variables, numbers start in register 2
PROG="find_max"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "3 0 0 0" "0"  no_elements
check_prog_output "10 0 0 1" "1"  only_1 
check_prog_output "10 1000 1000 1" "1" only_1b
check_prog_output "10 3000 4000 1 2 3 4 5 6 7" "7" 1_til_7
check_prog_output "20 0 0 3 56 83 12 9 66 2 7777 32 2222"  "7777" random 


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

