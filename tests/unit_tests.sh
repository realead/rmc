
PATTERN=${1:-*}
if [ "$PATTERN" = "all" ]; then
   PATTERN=*
fi

TESTCASE=${2:-.}


export PYTHONPATH="${PYTHONPATH}:exetest:."
export RMI=../src/rmi.py
export RMC=../src/rmc.py
python -m unittest discover "$TESTCASE" -p "test_$PATTERN.py" -v

