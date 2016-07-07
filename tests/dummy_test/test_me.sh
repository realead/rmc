############# SET UP ##################################
PROG="dummy_test"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5" "0"
check_prog_output "1 1" "1"
check_prog_output "23 235" "235"

#here are the test cases for program return value (errors)
check_prog_return "5 1" "0" #normal run
check_prog_return "1.4" "2" #input error - not a number, less than '0'
check_prog_return "" "4" no_arguments
check_prog_return "0" "5" zero_cells
check_prog_return "1 4 5" "6" more_inizialized_then_cells

################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

