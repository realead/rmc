


export RMI=../../src/rmi.py
export RMC=../../src/rmc.py
export RMJIT=../../src/rmjit.py


#MAX="100"
MAX="100000"
MAX="1000000"
#MAX="10000000" #for these values rmi is just too slow
#MAX="1000000000"

echo "Testing RMC: "
python $RMC -c time_test.rm -o time_test.exe
time ./time_test.exe 2  "$MAX"

rm *.s
rm *.o
rm *.exe



echo "\n\nTesting RMI: "
time python $RMI -f time_test.rm -n 2 -i "$MAX"


echo "\n\nTesting RMJIT: "
time python $RMJIT -f time_test.rm -n 2 -i "$MAX"

