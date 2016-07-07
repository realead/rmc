from rmcerrors import RMCError
import rmcerrors


 #OPERANDS:
        
class Constant:
    def __init__(self, constant_literal):
        self.constant=rmcerrors.asNonnegInt(constant_literal, lit_name="constant")
    
    def prepare_AMD64Mnemonics(self):
        return []
        
    def as_AMD64Mnemonics(self):
        return "${0}".format(self.constant)
        
             
class Register:
    def __init__(self, index_literal):
        self.index=rmcerrors.asNonnegInt(index_literal, lit_name="index")
    
    def prepare_AMD64Mnemonics(self):
        return ["movq\t${0}, %rcx".format(self.index)]#rcx <- index
           
    def as_AMD64Mnemonics(self):
        return "(%rdi, %rcx, 8)"#pointer to the registers is in %rdi
        
class Reference:
    def __init__(self, index_literal):
        self.index=rmcerrors.asNonnegInt(index_literal, lit_name="index")
    
    def prepare_AMD64Mnemonics(self):
        return ["movq\t${0}, %rcx".format(self.index),
                "movq\t(%rdi, %rcx, 8), %rcx"]#rcx <- value from REGS[index]
           
    def as_AMD64Mnemonics(self):
        return "(%rdi, %rcx, 8)"

#operand factory        
def createOperand(var_literal):
    if not var_literal:
        raise RMCError("operand expected, but none found")
    if var_literal[0]=='#':
        return Constant(var_literal[1:])
    if var_literal[0]=='*':
        return Reference(var_literal[1:])
    return Register(var_literal) 
     
        
#OPERATIONS        
class End:
    def __init__(self, operands):
        if operands:
           raise RMCError("END does not expect operands but {0} found".format(len(operands)))
             
    def as_AMD64Mnemonics(self):
        return ["jmp end_program"]


class Store:
    def __init__(self, operands):
        if len(operands)!=1:
           raise RMCError("STORE expects exact 1 operand but {0} found".format(len(operands)))
        self.operand=createOperand(operands[0])
        if isinstance(self.operand, Constant):
            raise RMCError("cannot store into a constant, need register or register reference")
             
    def as_AMD64Mnemonics(self):
        res=[]
        res.extend(self.operand.prepare_AMD64Mnemonics())
        res.append("movq\t%rax, "+self.operand.as_AMD64Mnemonics())
        return res
        

class Load:
    def __init__(self, operands):
        if len(operands)!=1:
           raise RMCError("LOAD expects exact 1 operand but {0} found".format(len(operands)))
        self.operand=createOperand(operands[0])
             
    def as_AMD64Mnemonics(self):
        res=[]
        res.extend(self.operand.prepare_AMD64Mnemonics())
        res.append("movq\t"+self.operand.as_AMD64Mnemonics()+", %rax")
        return res    
        
class Add:
    def __init__(self, operands):
        if len(operands)!=1:
           raise RMCError("ADD expects exact 1 operand but {0} found".format(len(operands)))
        self.operand=createOperand(operands[0])
             
    def as_AMD64Mnemonics(self):
        res=[]
        res.extend(self.operand.prepare_AMD64Mnemonics())
        res.append("addq\t"+self.operand.as_AMD64Mnemonics()+", %rax")
        return res   
        
                
#operation factory        
def createOperation(tokens):
    if not tokens:
        raise RMCError("operation expected, but none found")
    operation=tokens[0]
    operands=tokens[1:] 
    if operation == "END":
        return End(operands)
    if operation == "STORE":
        return Store(operands)
    if operation == "LOAD":
        return Load(operands) 
    if operation == "ADD":
        return Add(operands)   
        
    raise RMCError("unknown instruction "+operation);             
