from ascode import AssemblerCode

class RMParser:
    def __init__(self, input_file):
        with open(input_file,'r') as cin:
            self.lines=cin.readlines()
    
    def compile_file(self, compiler):
        self.compiler=compiler
        self.compiler.parser=self
        self.compiler.register_global_function("c2i", self.compiler.c2i_assembler_function())
        self.compiler.emit_main()
        self.compiler.close_output()#make sure the file is flushed
 
    def parse(self, code):
        if isinstance(code, AssemblerCode):
            self.compiler.write_assembler_code(code)
        else:
            pass     
