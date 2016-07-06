#################  SETUP  ######################################
RMRT_PATH="../../src/rmrt"
PROG="prog"

##################  BUILD #####################################

RMRT_SOURCES=$(ls $RMRT_PATH/*.s)

for source in $RMRT_SOURCES
do
  base=$(basename $source ".s")
  as -I$RMRT_PATH $source -o $base.o
done

as program.s -o program.o
OBJECTS=$(ls *.o)

ld $OBJECTS -o $PROG


############### RUN AND CHECK ################################

failed_cnt=0 #if everything ok return 0 - no example failed

# first parameter - command line arguments
# second parameter - expected program output
check_prog_output(){
    rec=$(./$PROG $1)
    if [ "$rec" != "$2" ]; then  
      echo "Wrong:received [$rec] vs. expected [$2]"
      failed_cnt=$((failed_cnt+1))
    fi
}

# first parameter - command line arguments
# second parameter - expected program return value
check_prog_return(){
    ./$PROG $1 > /dev/null
    rec=$?
    if [ "$rec" != "$2" ]; then  
      echo "Wrong return value: received [$rec] vs. expected [$2]"
      failed_cnt=$((failed_cnt+1))
    fi
}

# here are the test cases for program output:
check_prog_output "5" "0"
check_prog_output "1 1" "1"
check_prog_output "23 0 2222" "0"
check_prog_output "2 3333333" "3333333"
check_prog_output "1 18446744073709551615" "18446744073709551615" #maximal unsigned long
check_prog_output "1 1234567890" "1234567890" #all digits 0-9
check_prog_output "1 0123456789" "123456789" #no leading zeros

#here are the test cases for program return value (errors)
check_prog_return "5 1" "0" #normal run
check_prog_return "1.4" "2" #input error - not a number, less than '0'
check_prog_return "1b2" "2" #input error - not a number, bigger than '9'
check_prog_return "12 4 3a" "2" #input error - not a number



############# CLEAN UP ######################################

#with option --keep?
if [ "$1" != "--keep" ]; then
    rm *.o
    rm prog
fi

############ return the number of failed test cases 
if [ $failed_cnt = "0" ]; then
    echo "Ok"
else
    echo "$failed_cnt  wrong example(s)"
fi

exit $failed_cnt



