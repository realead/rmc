from rmcerrors import RMCError
import rmcerrors

#TODO make different modes for interpreter
MAX_REGISTER_VALUE=2**64

#Label:
class Label:
    def __init__(self, label_id, label_format="line{0}"):
        self.label_id=label_id
        self.label=label_format.format(self.label_id)
    
    def as_AMD64Mnemonics(self):
        return [self.label+":"]
        
    def as_reference(self):
        return self.label
        
        
#OPERANDS:

def encode64bit(z):
    res=''
    for i in xrange(8):
            res+=chr(z%256)
            z/=256;
    return res
    
class Constant:
    def __init__(self, constant_literal):
        self.constant=rmcerrors.asNonnegInt(constant_literal, lit_name="constant")
    
    def  get_value(self):
        return self.constant
        
    def prepare_AMD64Mnemonics(self):
        return []
        
    def as_AMD64Mnemonics(self):
        return "${0}".format(self.constant)

    def to_rdx_in_x86_64_opcode(self):
        #as 64bit unsigned integer (don't try to make it 32 bit)
        #movabs $constant, %rdx
        return b'\x48\xba'+encode64bit(self.constant)

    def interpret(self, rmstate):
        return self.constant
        
             
class Register:
    def __init__(self, index_literal):
        self.index=rmcerrors.asNonnegInt(index_literal, lit_name="index")
    
    def prepare_AMD64Mnemonics(self):
        return ["movq\t${0}, %rcx".format(self.index)]#rcx <- index
           
    def as_AMD64Mnemonics(self):
        return "(%rdi, %rcx, 8)"#pointer to the registers is in %rdi

    def to_rdx_in_x86_64_opcode(self):
        res=b'\x48\xb9'+encode64bit(self.index) #movabs $index, %rcx
        res+=b'\x48\x8b\x14\xcf'                #mov (%rdi, %rcx, 8), %rdx
        return res  
                                 

    def from_rdx_in_x86_64_opcode(self):
        res=b'\x48\xb9'+encode64bit(self.index) #movabs $index, %rcx
        res+=b'\x48\x89\x14\xcf' #mov %rdx, (%rdi, %rcx, 8) 
        return res 
     
    def interpret(self, rmstate):
        return rmstate.REGS[self.index]

    def interpret_as_ref(self, rmstate):
        return self.index
        
class Reference:
    def __init__(self, index_literal):
        self.index=rmcerrors.asNonnegInt(index_literal, lit_name="index")
    
    def prepare_AMD64Mnemonics(self):
        return ["movq\t${0}, %rcx".format(self.index),
                "movq\t(%rdi, %rcx, 8), %rcx"]#rcx <- value from REGS[index]
           
    def as_AMD64Mnemonics(self):
        return "(%rdi, %rcx, 8)"

    def interpret(self, rmstate):
        return rmstate.REGS[rmstate.REGS[self.index]]

    def interpret_as_ref(self, rmstate):
        return rmstate.REGS[self.index]


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

    def get_needed_line_labels(self):
        return []

    def interpret(self, rmstate):
        rmstate.ended = True

    def as_x86_64_opcode(self):
        return [b'\xc3'] #ret

        
class Operation:
    def __init__(self, operands, name="UNKNOWN"):
        if len(operands)!=1:
           raise RMCError("{0} expects exact 1 operand but {1} found".format(name, len(operands)))
        self.operand=createOperand(operands[0])    
        
        
class Store(Operation):
    def __init__(self, operands):
        Operation.__init__(self, operands, "STORE")
        if isinstance(self.operand, Constant):
            raise RMCError("cannot store into a constant, need register or register reference")
             
    def as_AMD64Mnemonics(self):
        res=[]
        res.extend(self.operand.prepare_AMD64Mnemonics())
        res.append("movq\t%rax, "+self.operand.as_AMD64Mnemonics())
        return res
    
    def get_needed_line_labels(self):
        return []

    def interpret(self, rmstate):
        index = self.operand.interpret_as_ref(rmstate)
        rmstate.REGS[index] = rmstate.acc 

    def as_x86_64_opcode(self):
        res=b'\x48\x89\xc2'                             # mov %rax, %rdx
        res+= self.operand.from_rdx_in_x86_64_opcode()  # move from %rdx to operand
        return [res] 


class Load(Operation):
    def __init__(self, operands):  
        Operation.__init__(self, operands, "LOAD")
             
    def as_AMD64Mnemonics(self):
        res=[]
        res.extend(self.operand.prepare_AMD64Mnemonics())
        res.append("movq\t"+self.operand.as_AMD64Mnemonics()+", %rax")
        return res 
        
    def get_needed_line_labels(self):
        return []   

    def interpret(self, rmstate):
        rmstate.acc = self.operand.interpret(rmstate)

    def as_x86_64_opcode(self):
        res=self.operand.to_rdx_in_x86_64_opcode()  # move operand to %rdx
        res+=b'\x48\x89\xd0'                        # mov %rdx, %rax
        return [res]
               


    
class Add(Operation):
    def __init__(self, operands):
        Operation.__init__(self, operands, "ADD")
             
    def as_AMD64Mnemonics(self):
        res=[]
        res.extend(self.operand.prepare_AMD64Mnemonics())
        res.append("addq\t"+self.operand.as_AMD64Mnemonics()+", %rax")
        return res   

    def get_needed_line_labels(self):
        return []
        
    def interpret(self, rmstate):
        rmstate.acc += self.operand.interpret(rmstate)   
        rmstate.acc %= MAX_REGISTER_VALUE     
        
class Mult(Operation):
    def __init__(self, operands):  
        Operation.__init__(self, operands, "MULT")
             
    def as_AMD64Mnemonics(self):
        res=[]
        res.extend(self.operand.prepare_AMD64Mnemonics())
        res.append("imulq\t"+self.operand.as_AMD64Mnemonics()+", %rax")
        return res   
              
    def get_needed_line_labels(self):
        return [] 
        
    def interpret(self, rmstate):
        rmstate.acc *= self.operand.interpret(rmstate)
        rmstate.acc %= MAX_REGISTER_VALUE         
        
 
class Sub(Operation):
    sub_cnt=0
    def __init__(self, operands): 
        Operation.__init__(self, operands, "SUB")
        #getting unique id used for the jump
        self.sub_id=Sub.sub_cnt
        Sub.sub_cnt+=1
             
    def as_AMD64Mnemonics(self):
        res=[]
        label_normal="sub{0}_jmp_label".format(self.sub_id)
        label_end="sub{0}_jmp_label_end".format(self.sub_id)     
        res.extend(self.operand.prepare_AMD64Mnemonics())
        res.append("cmpq\t"+self.operand.as_AMD64Mnemonics()+", %rax")
        res.append("ja "+label_normal) #jump to then branch
        res.append("movq\t $0, %rax") # else branch
        res.append("jmp "+label_end)  #jump over the then branch
        res.append(label_normal+":")
        res.append("subq\t"+self.operand.as_AMD64Mnemonics()+", %rax")
        res.append(label_end+":")
        return res   
     
    def get_needed_line_labels(self):
        return []
        
    def interpret(self, rmstate):
        rmstate.acc -= min(rmstate.acc, self.operand.interpret(rmstate)) #result cannot be negative 
           
        

class Div(Operation):
    def __init__(self, operands):
        Operation.__init__(self, operands, "DIV")
             
    def as_AMD64Mnemonics(self):
        res=[]
        res.extend(self.operand.prepare_AMD64Mnemonics())
        res.append("movq\t"+self.operand.as_AMD64Mnemonics()+", %rbx")
        res.append("xorl\t %edx, %edx")#edx must be 0
        res.append("divq\t%rbx")#rax<-rax/rbx
        return res  

    def get_needed_line_labels(self):
        return []
       
    def interpret(self, rmstate):
        rmstate.acc //= self.operand.interpret(rmstate) 


class Jump:
    def __init__(self, operands, name="UNKNOWN"):
        if len(operands)!=1:
           raise RMCError("{0} expects exact 1 operand but {1} found".format(name, len(operands)))
        const_val=createOperand(operands[0])  
        if not isinstance(const_val, Constant):
            raise RMCError(name+" label must be a const, but is "+operands[0])
        if const_val.get_value()<=0:
            raise RMCError(name+" label must positive, but is {0}".format(const_val.get_value()))      
        self.label=Label(const_val.get_value())  

class Goto(Jump):
    def __init__(self, operands):
        Jump.__init__(self, operands, "GOTO")           
             
    def as_AMD64Mnemonics(self):
        return ["jmp\t"+self.label.as_reference()]

    def interpret(self, rmstate):
        rmstate.b=self.label.label_id-1#-1=>account for automatical b+1 in every step
       
    def get_needed_line_labels(self):
        return [self.label.label_id]
 


class Jzero(Jump):
    def __init__(self, operands):  
        Jump.__init__(self, operands, "JZERO")    
                 
    def as_AMD64Mnemonics(self):
        return ["cmpq $0, %rax", "je\t"+self.label.as_reference()]

    def interpret(self, rmstate):
        if rmstate.acc==0:
            rmstate.b=self.label.label_id-1#-1=>account for automatical b+1 in every step
        
    def get_needed_line_labels(self):
        return [self.label.label_id]
 
  
 

MnemonicDictionary={"END":End, "STORE":Store, 
                    "LOAD":Load, "ADD":Add, 
                    "MULT":Mult, "SUB":Sub, 
                    "DIV":Div, "GOTO":Goto,
                    "JZERO":Jzero}                
#operation factory        
def createOperation(tokens):
    if not tokens:
        raise RMCError("operation expected, but none found")
    operation=tokens[0]
    operands=tokens[1:] 
    if operation not in MnemonicDictionary:
        raise RMCError("unknown instruction "+operation)
        
    return MnemonicDictionary[operation](operands)  
    
                   
