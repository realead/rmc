############# SET UP ##################################
#sub from 100 4 times the value in 0
PROG="goto"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "100" 
check_prog_output "1 1" "96"   
check_prog_output "1 24" "4"   only_24
check_prog_output "1 25" "0"  exact
check_prog_output "3 26" "0" overflow
  


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

