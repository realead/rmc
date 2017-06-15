#options


TEST_CASE=${1:-all}
KEEP=$2

### paths for all testing scripts
export RMC="python2.7 ../../src/rmc.py"
export TOOLS="../tools"

######## RUN ###################

error_cnt=0

#$1 directory
#$2 whether to keep
test_case(){
     cd "$1"
     echo "Test $1:"
     sh test_me.sh $KEEP
     error_cnt=$(($error_cnt+$?))
     cd ..
}


if [ $TEST_CASE = "all"  ]; then
    for d in *; do
        if [ -d "$d" ] && [ $d != "tools" ] && [ $d != "exetest" ]; then
             test_case $d
        fi
    done
else
   test_case $TEST_CASE
fi 

if [ $error_cnt != "0" ]; then
    echo "\nTHERE WERE $error_cnt ERRORS\n"
    return 1
else
    echo "\nall tests were ok\n"
    return 0
fi

