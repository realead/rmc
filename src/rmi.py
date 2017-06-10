#interpreter of the register machine language
#
# call python rmi.py N val1 ... valN < prog.rm
#
#
# for the file "prog.rm" to be interpreted, the register machine will have N memory cells initialized with values val1...valN at the beginning (if not given the initial value is 0)
 
import sys

#part1: parse input:

if len(sys.argv)<2:
   print >> sys.stderr, "error in set up: the number of registers must be given via command line\n"
   exit(1)

nREG = int(sys.argv[1])
iniVals =  map(int, sys.argv[2::])

if len(iniVals)>nREG:
   print >> sys.stderr, "error in set up: there are more initial values than registers\n"
   exit(1)    


REGS=iniVals+[0]*(nREG-len(iniVals))


#part2: interpret program

from rmclib.RMParser import RMParser as Parser
import rmclib.Interpreter

from rmclib.rmcerrors import RMCError 
try:
    rmprog = sys.stdin.readlines() 
    parser=Parser(rmprog)
    parsed_lines, needed_line_labels = parser.parse()

    result=rmclib.Interpreter.interpret(REGS, parsed_lines)

    print result
except RMCError as e:
    line_number=e.get_line_number()
    if line_number is None:
        print >> sys.stderr, "error compiling {0}: {1}".format(args.c, e)
    else :
        print >> sys.stderr, "error compiling {0} in line {1}: {2}".format(args.c, line_number, e)
    exit(1)



  

 
