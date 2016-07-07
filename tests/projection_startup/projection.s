# reads in the R0 which dimension should be projected and progects
#
#


.section .text
    .globl rmprogram
    .type rmprogram, @function
    
rmprogram:
    movq  REGS, %rdi            #get the pointer to REGS
    movq  (%rdi), %rax            #rax has index of the dimension
    movq  (%rdi, %rax, 8), %rbx
    movq  %rbx, (%rdi)
    retq
    
   
