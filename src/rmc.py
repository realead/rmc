##finding path to run_time

import sys
import os

path_to_rt=os.path.join(os.path.dirname(sys.argv[0]), "rmrt")



import argparse

parser = argparse.ArgumentParser(description='Register Machine Compiler')
parser.add_argument('-c', type=str,
                    help='file name of the file to compile')
parser.add_argument('-o', type=str, default="out.a",
                    help='file name of the resulting program')
parser.add_argument('-v', action='store_true',
                    help='verbosity flag')
parser.add_argument('-s', action='store_true',
                    help='only compiling')
                                        
args = parser.parse_args()


input_name=os.path.basename(args.c)
path, ext=os.path.splitext(args.c)
asm_file=path+".s"
obj_file=path+".o"


#compile rmprogram
from rmclib.RMParser import RMParser as Parser
from rmclib.AMD64Compiler import AMD64Compiler as Compiler

from rmclib.rmcerrors import RMCError 
try:
    parser=Parser(args.c)
    parsed_lines, needed_line_labels = parser.parse()

    compiler=Compiler(input_name)
    compiler.emit_main(parsed_lines, needed_line_labels)

    compiler.write_assembler_code_to_file(asm_file)
except RMCError as e:
    line_number=e.get_line_number()
    if line_number is None:
        print >> sys.stderr, "error compiling {0}: {1}".format(args.c, e)
    else :
        print >> sys.stderr, "error compiling {0} in line {1}: {2}".format(args.c, line_number, e)
    exit(1)



if args.s:
    exit(0)

#only if -s not set!

#assembly runtime:
command_list=[];
rt_files=["atouq", "error_exit", "print_newline", "startup", "uqtoa"]
for rt_file in rt_files:
    command_list.append(['as', "-I"+path_to_rt, os.path.join(path_to_rt, rt_file)+".s", '-o', rt_file+".o"])
    


#assembly rmprog
command_list.append(['as', asm_file, '-o', obj_file])

#link everything
command_list.append(['ld', '-o', args.o, obj_file]+[f+'.o' for f in rt_files])


#invoke the program:
import subprocess
for command in command_list:
    if args.v:
        print "calling:", ' '.join(command)
    subprocess.call(command)

  

 
