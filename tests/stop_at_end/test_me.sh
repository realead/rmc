############# SET UP ##################################
PROG="stop_at_end"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "0" no_ini
check_prog_output "1 0" "0" ini_is_0
check_prog_output "22 235 44" "235" ini_is_235

################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

