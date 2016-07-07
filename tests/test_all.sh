#options


TEST_CASE=${1:-all}
KEEP=$2

### paths for all testing scripts
export RMC="python2.7 ../../src/rmc.py"
export TOOLS="../tools"

######## RUN ###################

#$1 directory
#$2 whether to keep
test_case(){
     cd "$1"
     echo "Test $1:"
     sh test_me.sh $KEEP
     cd ..
}


if [ $TEST_CASE = "all"  ]; then
    for d in *; do
        if [ -d "$d" ] && [ $d != "tools" ]; then
             test_case $d
        fi
    done
else
   test_case $TEST_CASE
fi 


