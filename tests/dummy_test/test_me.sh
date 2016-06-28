RMC="python2.7 ../../src/rmc.py"

$RMC "-c" "dummy.rm" "-o" "dummy"
./dummy

test_result=$?
rm *.s
rm dummy

if [ $test_result = 42 ]; then
    echo "OK"
    exit 0
else
    echo "Wrong"
    exit 1
fi
