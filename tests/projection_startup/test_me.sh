#################  SETUP  ######################################
RMRT_PATH="../../src/rmrt"
TOOLS="../tools"
PROG="projection"

##################  BUILD #####################################

sh $RMRT_PATH/build_rmrt.sh "." 
sh $TOOLS/compile_and_link_all.sh $PROG 

############### RUN AND CHECK ################################

failed_cnt=0 #if everything ok return 0 - no example failed

# first parameter - command line arguments
# second parameter - expected program output
# third parameter (optional) - test case name
check_prog_output(){
    sh $TOOLS/check_output.sh ./$PROG "$1" "$2" "$3"
    failed_cnt=$((failed_cnt+$?))
}

# first parameter - command line arguments
# second parameter - expected program return value
# third parameter (optional) - test case name
check_prog_return(){
    sh $TOOLS/check_status.sh ./$PROG "$1" "$2" "$3"
    failed_cnt=$((failed_cnt+$?))
}

# here are the test cases for program output:
check_prog_output "5 2 3" "0" proj_2_unset
check_prog_output "5 0 1 2 3 4" "0" proj_0
check_prog_output "5 1 66 22 33 44" "66" proj_1
check_prog_output "5 2 11 22 66 44" "22" proj_2
check_prog_output "5 3 11 22 33 44" "33" proj_3
check_prog_output "5 4 1 2 3 44" "44" proj_4



############# CLEAN UP ######################################

#with option --keep?
if [ "$1" != "--keep" ]; then
    rm *.o
    rm projection
fi

############ return the number of failed test cases 
if [ $failed_cnt = "0" ]; then
    echo "Ok"
else
    echo "$failed_cnt  wrong example(s)"
fi

exit $failed_cnt



