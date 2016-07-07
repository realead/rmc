############# SET UP ##################################
PROG="move2_to_0"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "0"
check_prog_output "3 1 0 33" "33"
check_prog_output "23 235 11 0 333 44 " "0"
check_prog_output "23 0 11 15 333 44 " "15"

################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

