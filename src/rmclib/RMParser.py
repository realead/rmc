
from LineParser import LineParser
from rmcerrors import RMCError

class RMParser:
    def __init__(self, input_file):
        with open(input_file,'r') as cin:
            self.lines=cin.readlines()
 
    def parse(self, code):
        expected_b=1
        lines_of_end=[]
        parsed_lines=[]
        needed_line_labels=set()
        for number, line in enumerate(code):
            try:
                parsed_line=LineParser(line.strip())
                parsed_line.check_b(expected_b)
                parsed_line.add_to_end_list(lines_of_end)
                needed_line_labels.update(parsed_line.get_needed_line_labels())  
                parsed_lines.append(parsed_line)
                expected_b+=1
            except RMCError as e:
                e.set_line_number(number+1)
                raise
            
        #check whether there is an END instruction
        if len(lines_of_end)!=1:
            raise RMCError("exact one END instruction expected, but {0} found".format(len(lines_of_end)))
        
        if needed_line_labels and max(needed_line_labels)>len(parsed_lines):
            raise RMCError("unknown GOTO/JZERO label {0}, there are only {1} lines".format(max(needed_line_labels), len(parsed_lines)))

    
        return (parsed_lines, needed_line_labels)   
            
            
            
   
