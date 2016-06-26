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
        pass      
