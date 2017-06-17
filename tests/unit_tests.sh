

export PYTHONPATH="${PYTHONPATH}:exetest"
export RMI=../src/rmi.py
python -m unittest discover -p "test_rmi*.py" -v

