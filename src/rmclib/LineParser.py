#a line is: 
#
#otherwise:
#it looks as follows:
#XXX YYYY [ZZZ]
#with 
#    - XXX - line number
#    - YYY - operation name
#    - ZZZ - operand
#
#

import RMMnemonics as rms
import rmcerrors
from rmcerrors import RMCError 


    
class LineParser:
    def __init__(self, line):
        self.is_end=False
        self.line_label_needed=False
        parts=line.split()
        self.parse_b(parts[0])
        self.operation=rms.createOperation(parts[1:])
        self.is_end=isinstance(self.operation, rms.End)
                
        
    def as_AMD64Mnemonics(self):
        res=[]
        if self.line_label_needed:
            label=rms.Label(self.b)
            res.extend(label.as_AMD64Mnemonics())
        res.extend(self.operation.as_AMD64Mnemonics())
        return res

    def interpret(self, rmstate):
        self.operation.interpret(rmstate)

    def as_x86_64_opcode(self):
        return self.operation.as_x86_64_opcode()
                
    def parse_b(self, b_literal):
        self.b=rmcerrors.asNonnegInt(b_literal, must_be_positive=True, lit_name="b")
            
    def check_b(self, expected_b):
        if expected_b!=self.b:
            raise RMCError("expected b is {0}, found b is {1}".format(expected_b, self.b))  
    
    
    def set_line_label_as_needed(self):
        self.line_label_needed=True
        
        
    def get_needed_line_labels(self):
        return self.operation.get_needed_line_labels()        
            
    def add_to_end_list(self, list_of_ends):
        if self.is_end:
             list_of_ends.append(self.b)
             
             
