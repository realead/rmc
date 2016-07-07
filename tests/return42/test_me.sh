RMC="python2.7 ../../src/rmc.py"
TOOLS="../tools"
PROG="return42"


############### BUILD ########################################

$RMC "-c" "return42.rm" "-o" $PROG


############### RUN AND CHECK ################################

failed_cnt=0 #if everything ok return 0 - no example failed
all_cnt=0

# first parameter - command line arguments
# second parameter - expected program output
# third parameter (optional) - test case name
check_prog_output(){
    sh $TOOLS/check_output.sh ./$PROG "$1" "$2" "$3"
    failed_cnt=$((failed_cnt+$?))
    all_cnt=$((all_cnt+1))
}

# first parameter - command line arguments
# second parameter - expected program return value
# third parameter (optional) - test case name
check_prog_return(){
    sh $TOOLS/check_status.sh ./$PROG "$1" "$2" "$3"
    failed_cnt=$((failed_cnt+$?))
    all_cnt=$((all_cnt+1))
}

# here are the test cases for program output:
check_prog_output "5" "42"
check_prog_output "1 11" "42"
check_prog_output "23 235 11 0 333 44 " "42"



################# CLEAN UP ##########################################
#with option --keep?
if [ "$1" != "--keep" ]; then
    rm *.s
    rm *.o
    rm $PROG
fi

############ REPORT ################################################## 

if [ $failed_cnt = "0" ]; then
    echo "all $all_cnt tests Ok"
else
    echo "$failed_cnt  wrong example(s) out of $all_cnt tests"
fi

exit $failed_cnt

