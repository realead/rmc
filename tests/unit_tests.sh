
PATTERN=${1:-*}


export PYTHONPATH="${PYTHONPATH}:exetest"
export RMI=../src/rmi.py
export RMC=../src/rmc.py
python -m unittest discover -p "test_$PATTERN.py" -v

