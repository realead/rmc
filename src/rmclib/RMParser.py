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
 
    def parse(self, code):
        if isinstance(code, AssemblerCode):
            self.compiler.add_assembler_code(code)
        else:
            expected_b=1
            lines_of_end=[]
            parsed_lines=[]
            needed_line_labels=set()
            for line in code:
                parsed_line=LineParser(line.strip())
                parsed_line.check_b(expected_b)
                parsed_line.add_to_end_list(lines_of_end)
                needed_line_labels.update(parsed_line.get_needed_line_labels())  
                parsed_lines.append(parsed_line)
                expected_b+=1
                
            #check whether there is an END instruction
            if len(lines_of_end)!=1:
                raise RMCError("exact one END instruction expected, but {0} found".format(len(lines_of_end)))
            
            if needed_line_labels and max(needed_line_labels)>len(parsed_lines):
                raise RMCError("unknown GOTO/JZERO label {0}, there are only {1} lines".format(max(needed_line_labels), len(parsed_lines)))
            #put it into the assembler code:
            asm_code=AssemblerCode()
            for (b_, parsed_line) in enumerate(parsed_lines):
                b=b_+1
                if b in needed_line_labels:
                    parsed_line.set_line_label_as_needed()
                mnemonics=parsed_line.as_AMD64Mnemonics()
                for mnemonic in mnemonics:
                    if mnemonic:
                        asm_code.append_tabbed_line(mnemonic)
            
                
            self.compiler.add_assembler_code(asm_code)
            
            
            
   
