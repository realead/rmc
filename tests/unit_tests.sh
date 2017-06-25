
PATTERN=${1:-*}
if [ "$PATTERN" = "all" ]; then
   PATTERN=*
fi

TESTCASE=${2:-.}

if [ "$3" = "--keep" ]; then
    export KEEP="YES"
fi


export PYTHONPATH="${PYTHONPATH}:exetest:."
export RMI=../src/rmi.py
export RMC=../src/rmc.py
export RMJIT=../src/rmjit.py
python -m unittest discover "$TESTCASE" -p "test_$PATTERN.py" -v

