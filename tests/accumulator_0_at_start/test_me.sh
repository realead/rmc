############# SET UP ##################################
PROG="accumulator_0_at_start"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "0" nothing_initialized
check_prog_output "1 1" "0" initialized_with_1
check_prog_output "23 235 22 22" "0" initialized_with_235

################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt
