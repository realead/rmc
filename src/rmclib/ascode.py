
class AssemblerCode:

    def __init__(self):
        self.code=[]
        
    def append_code_line(self, line):
        self.code.append(line+'\n')
    
    def append_tabbed_line(self, line):
        self.append_code_line('\t'+line)
        
    def extend_code(self, assembler_lines):
        self.code.extend(assembler_lines.code)
    
    def append_comment(self, comment):
        self.append_code_line('/*'+comment+'*/')
            
    def write_to_file(self, f):
        f.writelines(self.code)

	
