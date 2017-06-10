
from ascode import AssemblerCode

class AMD64CompilerException(Exception):
    pass


class AMD64Compiler:
    def __init__(self, input_file, parser=None):
        #needed counters:
        self.mangled_funs=set()
        
        self.parser=parser
        self.assembler=AssemblerCode()
        
        self.assembler.append_tabbed_line('.file\t"{0}"'.format(input_file))
        self.assembler.append_tabbed_line('.text')
        
        
    def compile_lines(self, parsed_lines, needed_line_labels):
        asm_code=AssemblerCode()
        for (b_, parsed_line) in enumerate(parsed_lines):
            b=b_+1
            if b in needed_line_labels:
                parsed_line.set_line_label_as_needed()
            mnemonics=parsed_line.as_AMD64Mnemonics()
            for mnemonic in mnemonics:
                if mnemonic:
                    asm_code.append_tabbed_line(mnemonic)
        return asm_code

         
    def register_global_function(self, mangled_fun_name, fun_body):
        if mangled_fun_name in self.mangled_funs:
            raise AMD64CompilerException("redefinition of function "+mangled_fun_name)
        
        #remember function   
        fun_id=len(self.mangled_funs)
        self.mangled_funs.add(mangled_fun_name)
        
        #prolog:
        self.assembler.append_tabbed_line('.globl\t{0}'.format(mangled_fun_name))
        self.assembler.append_tabbed_line('.type\t{0}, @function'.format(mangled_fun_name))
        self.assembler.append_code_line('{0}:'.format(mangled_fun_name))
        
        #setting up the enviroment
        self.assembler.append_tabbed_line('movq\tREGS, %rdi')
        self.assembler.append_tabbed_line('movq\t$0, %rax')
         
        #inner_part
        
	    #code of the function	
        parsed_lines, needed_line_labels=self.parser.parse(fun_body)
        self.add_assembler_code(self.compile_lines(parsed_lines, needed_line_labels))

        self.assembler.append_code_line('end_program:')
        self.assembler.append_tabbed_line('ret')
             
           
    def emit_main(self, inner_code):   
        self.register_global_function("rmprogram", inner_code)
        
        
    def add_assembler_code(self, code):
        self.assembler.extend_code(code)    
        
    def write_assembler_code_to_file(self, output_file_name):
        with open(output_file_name, "w") as f:
            self.assembler.write_to_file(f)
        
