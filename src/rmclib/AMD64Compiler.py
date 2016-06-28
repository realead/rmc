
from ascode import AssemblerCode

class AMD64CompilerException(Exception):
    pass


class AMD64Compiler:
    def __init__(self, output_file, input_file, parser=None):
        #needed counters:
        self.mangled_funs=set()
        
        self.parser=parser
        
        self.out=open(output_file, 'w')
        self.out.write('\t.file\t"{0}"\n'.format(input_file))
        self.out.write('\t.text\n')
    
    def write_assembler_code(self, assembler_code):
        assembler_code.write_to_file(self.out)
        
            
    def register_global_function(self, mangled_fun_name, fun_body):
        if mangled_fun_name in self.mangled_funs:
            raise AMD64CompilerException("redefinition of function "+mangled_fun_name)
        
        #remember function   
        fun_id=len(self.mangled_funs)
        self.mangled_funs.add(mangled_fun_name)
        
        #prolog:
        code=AssemblerCode()
        code.append_tabbed_line('.globl\t{0}'.format(mangled_fun_name))
        code.append_tabbed_line('.type\t{0}, @function'.format(mangled_fun_name))
        code.append_code_line('{0}:'.format(mangled_fun_name))
        code.append_code_line('.LFB{0}:'.format(fun_id))
        
        #inner_part
        code.append_tabbed_line('.cfi_startproc')
        code.append_tabbed_line('pushq\t%rbp')
        code.append_tabbed_line('.cfi_def_cfa_offset 16')
        code.append_tabbed_line('.cfi_offset 6, -16')
        code.append_tabbed_line('movq\t%rsp, %rbp')
        code.append_tabbed_line('.cfi_def_cfa_register 6')
	    
	    #error if something wrong
        code.append_tabbed_line('movl\t$1, %eax')
	    
	    #code of the function	
        self.parser.parse(fun_body)
        
        #no errors
        code.append_tabbed_line('movl\t$42, %eax')
        
        #cleaning up
        code.append_tabbed_line('popq\t%rbp')
        code.append_tabbed_line('.cfi_def_cfa 7, 8')
        code.append_tabbed_line('ret')
        code.append_tabbed_line('.cfi_endproc')
        
        #epilog:
        code.append_code_line('.LFE{0}:'.format(fun_id))
        code.append_tabbed_line('.size\t{0}, .-{0}'.format(mangled_fun_name))
        
        #flush to the file:
        self.write_assembler_code(code)
            
    def emit_main(self, inner_code):
        self.register_global_function("main", inner_code)
        
    def close_output(self):
        self.out.close()
        
        
    def c2i_assembler_function(self):
        code=AssemblerCode()
        
        code.append_tabbed_line('movq\t%rdi, -24(%rbp)')
        code.append_tabbed_line('movl\t$0, -4(%rbp)')
        code.append_tabbed_line('jmp\t.L2')
        code.append_code_line('.L3:')
        code.append_tabbed_line('movl\t-4(%rbp), %edx')
        code.append_tabbed_line('movl\t%edx, %eax')
        code.append_tabbed_line('sall\t$2, %eax')
        code.append_tabbed_line('addl\t%edx, %eax')
        code.append_tabbed_line('addl\t%eax, %eax')
        code.append_tabbed_line('movl\t%eax, %edx')
        code.append_tabbed_line('movq\t-24(%rbp), %rax')
        code.append_tabbed_line('movzbl\t(%rax), %eax')
        code.append_tabbed_line('movsbl\t%al, %eax')
        code.append_tabbed_line('subl\t$48, %eax')
        code.append_tabbed_line('addl\t%edx, %eax')
        code.append_tabbed_line('movl\t%eax, -4(%rbp)')
        code.append_tabbed_line('addq\t$1, -24(%rbp)')
        code.append_code_line('.L2:')
        code.append_tabbed_line('movq\t-24(%rbp), %rax')
        code.append_tabbed_line('movzbl\t(%rax), %eax')
        code.append_tabbed_line('testb\t%al, %al')
        code.append_tabbed_line('jne\t.L3')
        code.append_tabbed_line('movl\t-4(%rbp), %eax')
        
        return code

	
