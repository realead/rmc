import argparse

parser = argparse.ArgumentParser(description='Register Machine Compiler')
parser.add_argument('-c', type=str,
                    help='file name of the file to compile')
parser.add_argument('-o', type=str, 
                    help='file name of the resulting program')
                    
args = parser.parse_args()

import os

input_name=os.path.basename(args.c)
path, ext=os.path.splitext(args.c)
asm_file=path+".s"

from rmclib.RMParser import RMParser as Parser
from rmclib.AMD64Compiler import AMD64Compiler as Compiler

parser=Parser(args.c)
compiler=Compiler(asm_file, input_name, parser)

parser.compile_file(compiler)

#start  gcc:
import subprocess
command=['gcc', asm_file,'-o', args.o]
subprocess.call(command)

#print"result:", subprocess.check_output(command, stderr=subprocess.STDOUT)

 
