

export PYTHONPATH="${PYTHONPATH}:exetest"
export RMI=../src/rmi.py
python -m unittest discover -p "*_rmi_*.py" -v

