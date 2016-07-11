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
        parts=line.split()
        self.parse_b(parts[0])
        self.operation=rms.createOperation(parts[1:])
        self.is_end=isinstance(self.operation, rms.End)
                
        
    def as_AMD64Mnemonics(self):
        return self.operation.as_AMD64Mnemonics()
        
          
    def parse_b(self, b_literal):
        self.b=rmcerrors.asNonnegInt(b_literal, must_be_positive=True, lit_name="b")
            
    def check_b(self, expected_b):
        if expected_b!=self.b:
            raise RMCError("expected b is {0}, found b is {1}".format(expected_b, self.b))  
    
    def get_needed_line_labels(self):
        return self.operation.get_needed_line_labels()        
            
    def add_to_end_list(self, list_of_ends):
        if self.is_end:
             list_of_ends.append(self.b)
             
             
