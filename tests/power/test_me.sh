############# SET UP ##################################
#calls 0^1, needs at least 3 registers
PROG="power"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "3 0 0 0" "1" 
check_prog_output "3 5 0" "1"   
check_prog_output "3 2 64 444" "0" overflow 
check_prog_output "3 5 4" "625" 5^4
check_prog_output "3 2 63"  "9223372036854775808" 2^63 


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

