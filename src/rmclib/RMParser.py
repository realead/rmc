from ascode import AssemblerCode
from LineParser import LineParser
from rmcerrors import RMCError

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
            expected_b=1
            lines_of_end=[]
            for line in code:
                parsed_line=LineParser(line.strip())
                parsed_line.check_b(expected_b)
                parsed_line.add_to_end_list(lines_of_end)
                    
                mnemonics=parsed_line.as_AMD64Mnemonics()
                for mnemonic in mnemonics:
                    if mnemonic:
                        asm_code.append_tabbed_line(mnemonic)
                expected_b+=1
                
            #check whether there is an END instruction
            if len(lines_of_end)!=1:
                raise RMCError("exact one END instruction expected, but {0} found".format(len(lines_of_end)))
            
                
            self.compiler.write_assembler_code(asm_code)
            
            
            
   
