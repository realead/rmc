from ascode import AssemblerCode
from LineParser import LineParser

class RMParser:
    def __init__(self, input_file):
        with open(input_file,'r') as cin:
            self.lines=cin.readlines()
    
    def compile_file(self, compiler):
        self.compiler=compiler
        self.compiler.parser=self
        self.compiler.emit_main(self.lines)
        self.compiler.close_output()#make sure the file is flushed
 
    def parse(self, code):
        if isinstance(code, AssemblerCode):
            self.compiler.write_assembler_code(code)
        else:
            asm_code=AssemblerCode()
            for line in code:
                mnemonics=LineParser(line.strip()).get_instruction().as_mnemonic()
                for mnemonic in mnemonics:
                    if mnemonic:
                        asm_code.append_tabbed_line(mnemonic)
            self.compiler.write_assembler_code(asm_code)
            
            
            
   
