#interpreter of the register machine language
#
# call python rmi.py N val1 ... valN < prog.rm
#
#
# for the file "prog.rm" to be interpreted, the register machine will have N memory cells initialized with values val1...valN at the beginning (if not given the initial value is 0)
 
import sys
import argparse


#part1, parse input:
parser = argparse.ArgumentParser(description='Register Machine Interpreter')

parser.add_argument('-f',  type=str, 
                    help="file with the register machine program which should be interpreted")
parser.add_argument('-d',  type=str, default=None,
                    help="dumps jit-code to this file, which can be disassembled via    'objdump -b binary -D FILE_NAME -m i386:x86-64'")
parser.add_argument('-n', type=str, default=None,
                    help='number of registers')
parser.add_argument('-i', type=str, 
                    help='space separated list of initial values of the registers')


args = parser.parse_args()

if args.n is None:
    exit(4)

try:
    nREG = int(args.n)
except:
    exit(2)#not a number

if nREG<0:
    exit(2)#not a number, the same as rmc-result

if nREG==0:
    exit(5)#no registers

try:
    iniVals =  map(int, args.i.split()) if args.i is not None else []
except:
    exit(2)#not a number


if len(iniVals)>nREG:
   exit(6)    


REGS=iniVals+[0]*(nREG-len(iniVals))


#part2: interpret program

from rmclib.RMParser import RMParser as Parser
import rmclib.JITCompiler

from rmclib.rmcerrors import RMCError 
try:
    with open(args.f, 'r') as f:
        rmprog = f.readlines()

    parser=Parser(rmprog)
    parsed_lines, needed_line_labels = parser.parse()

except RMCError as e:
    line_number=e.get_line_number()
    if line_number is None:
        print >> sys.stderr, "error compiling {0}: {1}".format(args.f, e)
    else :
        print >> sys.stderr, "error compiling {0} in line {1}: {2}".format(args.f, line_number, e)
    exit(1)


#try:
result=rmclib.JITCompiler.jitrun(REGS, parsed_lines, args.d)
print result
#except Exception as e:
#    print >> sys.stderr, "run time error {0}".format(e)
#    exit(1)



  

 
