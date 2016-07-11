############# SET UP ##################################
#calls 0!, needs at least 2 registers
PROG="factorial"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "2 0 0" "1"  "0!"
check_prog_output "2 1 0" "1"  "1!" 
check_prog_output "2 2 64" "2" "2!"
check_prog_output "2 3 4" "6" "3!"
check_prog_output "2 4 63"  "24" "4!" 
check_prog_output "2 5"  "120" "5!" 


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

