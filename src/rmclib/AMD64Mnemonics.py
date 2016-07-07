


#We use %rax register as Accumulator
class Accumulator:
    def __init__(self, name="rax"):
        self.name=name
    
    def prepare(self):
        return []
            
    def as_mnemonic(self):
        return "%"+self.name
        
        
class Constant:
    def __init__(self, constant):
        self.constant=constant
    
    def prepare(self):
        return []
        
    def as_mnemonic(self):
        return "${0}".format(self.constant)
        

        
        
#operation with 2 operands        
class Operation2: 
    def __init__(self, oper_mnem, first_op, second_op):
        self.oper_mnem=oper_mnem
        self.first=first_op
        self.second=second_op
        
    def as_mnemonic(self):
        res=[]
        res.extend(self.first.prepare())
        res.extend(self.second.prepare())
        res.append(self.oper_mnem+"\t"+self.first.as_mnemonic()+", "+self.second.as_mnemonic())
        return res
        
         
#registers are pointed to by REGS pointer      
class Register:
    def __init__(self, index):
        self.index=index
    
    def prepare(self):
        return Operation2("movq", Constant(self.index), Accumulator("rcx")).as_mnemonic()
           
    def as_mnemonic(self):
        return "(%rdi, %rcx, 8)"
        
             
