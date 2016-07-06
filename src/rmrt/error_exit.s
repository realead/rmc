#this function ends the program

#%rdi -> error code which should be returned

.include "linux64.h"

.section .text
    .globl error_exit
    .type error_exit, @function
    
error_exit:
    
    #Exit with status which is saved in %rdi
    movq  $SYS_EXIT, %rax
    syscall
    
    
