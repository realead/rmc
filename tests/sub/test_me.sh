############# SET UP ##################################
#sub from 100 const 5, value in 0 und refereced by 1
PROG="sub"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "95" 
check_prog_output "2 1 0" "93"   
check_prog_output "3 2 1 0" "92"  


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

