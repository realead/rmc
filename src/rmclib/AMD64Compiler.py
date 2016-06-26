

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
        
    def register_global_function(self, mangled_fun_name, fun_body):
        if mangled_fun_name in self.mangled_funs:
            raise AMD64CompilerException("redefinition of function "+mangled_fun_name)
        
        #remember function   
        fun_id=len(self.mangled_funs)
        self.mangled_funs.add(mangled_fun_name)
        
        #prolog:
        self.out.write('\t.globl\t{0}\n'.format(mangled_fun_name))
        self.out.write('\t.type\t{0}, @function\n'.format(mangled_fun_name))
        self.out.write('{0}:\n'.format(mangled_fun_name))
        self.out.write('.LFB{0}:\n'.format(fun_id))
        
        #inner_part
        self.out.write('\t.cfi_startproc\n')
        self.out.write('\tpushq\t%rbp\n')
        self.out.write('\t.cfi_def_cfa_offset 16\n')
        self.out.write('\t.cfi_offset 6, -16\n')
        self.out.write('\tmovq\t%rsp, %rbp\n')
        self.out.write('\t.cfi_def_cfa_register 6\n')
	    
	    #error if something wrong
        self.out.write('\tmovl\t$1, %eax\n')
	    
	    #code of the function	
        self.parser.parse(fun_body)
        
        #no errors
        self.out.write('\tmovl\t$0, %eax\n')
        
        #cleaning up
        self.out.write('\tpopq\t%rbp\n')
        self.out.write('\t.cfi_def_cfa 7, 8\n')
        self.out.write('\tret\n')
        self.out.write('\t.cfi_endproc\n')
        
        #epilog:
        self.out.write('.LFE{0}:\n'.format(fun_id))
        self.out.write('\t.size\t{0}, .-{0}\n'.format(mangled_fun_name))
            
    def emit_main(self, inner_code):
        self.register_global_function("main", inner_code)
        
    def close_output(self):
        self.out.close()

	
