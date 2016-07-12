
#1. argument -> program name
build(){
    $RMC "-c" "$1.rm" "-o" $1
}



failed_cnt=0 #if everything ok return 0 - no example failed
all_cnt=0


#1. argument -> file to compile, also test case name
#2. expected error message
#3. expected error line
only_compile(){
    NAME=$1
    if [ -z ${3+x} ]; then 
        #line is unset
        EXPECTED="error compiling $NAME.rm: $2"
    else
        #line number is set 
        EXPECTED="error compiling $NAME.rm in line $3: $2"
    fi
    #capturing only the stderr
    ERROR_MESSAGE=$($RMC -s "-c" "$NAME.rm" 2>&1 1>/dev/null)
    if [ "$ERROR_MESSAGE" != "$EXPECTED" ]; then  
        echo "TC $NAME, output is wrong: received [$ERROR_MESSAGE] vs. expected [$EXPECTED]"
        failed_cnt=$((failed_cnt+1))
    fi
    all_cnt=$((all_cnt+1))
}


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
