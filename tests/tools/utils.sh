
#1. argument -> program name
build(){
    $RMC "-c" "$1.rm" "-o" $1
}


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


clean_up(){
    #with option --keep?
    if [ "$1" != "--keep" ]; then
        rm *.s
        rm *.o
        rm $PROG
    fi
}


report(){
    if [ $failed_cnt = "0" ]; then
        echo "all $all_cnt tests Ok"
    else
        echo "$failed_cnt  wrong example(s) out of $all_cnt tests"
    fi
}
