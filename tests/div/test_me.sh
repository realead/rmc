############# SET UP ##################################
#div 120 by const 5, by value in 0 und by refereced by 1
PROG="div"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5 1 0" "24" 
check_prog_output "2 4 1" "6"   
check_prog_output "3 1 2 7" "3"  


################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

