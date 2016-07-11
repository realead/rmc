############# SET UP ##################################
#if 0.th cell is 0 than copy 1. cell into 0 otherwise the 2. cell
PROG="jzero"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "0" 
check_prog_output "3 1 5 6" "6" take_second   
check_prog_output "3 2 5 6" "6" take_second2 
check_prog_output "3 0 5 6" "5" take_first 
  


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

