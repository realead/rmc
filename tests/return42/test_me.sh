############# SET UP ##################################
PROG="return42"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "42"
check_prog_output "1 11" "42"
check_prog_output "23 235 11 0 333 44 " "42"

################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

