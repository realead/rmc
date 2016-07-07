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

import AMD64Mnemonics
from rmcerrors import RMCError 



    
class LineParser:
    def __init__(self, line):
        self.is_end=False
        parts=line.split()
        self.parse_b(parts[0])
        self.operation=parts[1]
        if self.operation=="END":
            self.is_end=True
            if len(parts)>2:
                raise RMCError("no operand for END expected, but found "+parts[2])
        else:
            self.operand=parts[2]
        
    def get_operand(self):
        if self.operand[0]=='#': #we have a constant!
            return AMD64Mnemonics.Constant(int(self.operand[1:]))
        if self.operand[0]=='*': #we have a reference
            return None #not yet implemented
        #ok we have a normal register
        return AMD64Mnemonics.Register(int(self.operand))
        
        
    def get_instruction(self):
        if self.operation=="STORE":
           return AMD64Mnemonics.Operation2("movq", AMD64Mnemonics.Accumulator(), self.get_operand())
           
       
        if self.operation=="LOAD":
           return AMD64Mnemonics.Operation2("movq", self.get_operand(), AMD64Mnemonics.Accumulator())
           
        if self.operation=="END":
            return AMD64Mnemonics.End()
           
        raise RMCError("unknown instruction "+self.operation); 
          
    def parse_b(self, b_literal):
        if not b_literal.isdigit():
            raise RMCError("b must be a positive integer, found "+b_literal)
        self.b=int(b_literal)
        if not self.b:
            raise RMCError("b must be a positive integer, found "+b_literal) 
            
    def check_b(self, expected_b):
        if expected_b!=self.b:
            raise RMCError("expected b is {0}, found b is {1}".format(expected_b, self.b))  
            
            
    def add_to_end_list(self, list_of_ends):
        if self.is_end:
             list_of_ends.append(self.b)
