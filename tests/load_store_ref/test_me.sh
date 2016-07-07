############# SET UP ##################################
#load value from the cell pointed by 0, store to the cell pointed by 1, load from this cell, put to as  answer
PROG="load_store_ref"

#load functions:

. $TOOLS/utils.sh

############### BUILD ########################################

build $PROG

############### RUN AND CHECK ################################
# here are the test cases for program output:
check_prog_output "5 1 2" "2" 
check_prog_output "2 0 0" "0" goal_is_0  
check_prog_output "23 2 22 444" "444" goal_is_last_cell

################# CLEAN UP ##########################################
KEEP=$1
clean_up $KEEP

############ REPORT ################################################## 
report

exit $failed_cnt

