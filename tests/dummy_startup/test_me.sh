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


# here are the test cases:
check_prog_output "5" "0"

############# CLEAN UP ######################################

#with option --keep?
if [ "$1" != "--keep" ]; then
    rm *.o
    rm prog
fi

############ return the number of failed test cases 
exit $failed_cnt



