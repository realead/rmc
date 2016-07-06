#print new line character to a file
#
#file to write in %rdi 
#


.include "linux64.h"

.section .data
newline:
    .ascii "\n"
    
.section .text
    .globl print_newline  
    .type print_newline, @function
    
print_newline:
    movq  $SYS_WRITE, %rax        #write to
    #                             #rdi is already the file id
    movq  $newline, %rsi          #this buffer
    movq  $1, %rdx                #only one byte                          
    syscall
    
    retq
    
