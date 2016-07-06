# this function converts a \0 terminated string into its numeric value
# assuming it is base-10 unsigned long long int (unsigned quad)
#
#no error treatment yet
#
#
#input:
#%rdi -> pointer to the \0 terminated string
#
#output:
#%rax -> the resulting number
#

.include "error_codes.h"

.section .text
    .globl atouq
    .type atouq, @function
    
atouq:

    movq $0, %rax
    
start_loop:
    movb (%rdi), %bl
    cmpb $0, %bl
    je loop_exit

test_ge_0: 
    cmpb $'0', %bl
    jge test_le_9
    
    #error ch<'0':
    movq $ERROR_WRONG_CHAR, %rdi
    call error_exit

test_le_9:
    cmpb  $'9', %bl
    jle digit
    
    #error ch>'9':
    movq $ERROR_WRONG_CHAR, %rdi
    call error_exit 
       
digit:   
    imulq $10, %rax
    subb $'0', %bl
    movzbq %bl, %rcx
    add %rbx, %rax
    incq %rdi
    jmp start_loop
    
    
loop_exit:
    retq
    
    
