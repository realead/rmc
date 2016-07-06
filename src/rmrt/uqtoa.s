# this function converts an unsigned long long integer (unsigned quad) to a \0 terminated string base 10 representation ot the number
#
#no error treatment yet
#
#input:
#%rdi -> number to be converted
#%rsi -> pointer to the buffer
#
#output:
#%rax -> the resulting number (whithout \0)
#buffer contains the number
#%rsi -> shows to address directly after the last \0
#

.section .text
    .globl uqtoa
    .type uqtoa, @function
    
uqtoa:

    movq $0, %rcx #(length of the string without \0)
    movq %rdi, %rax
    movq $10, %rbx
put_next_char_onto_stack:
    cmpq $0, %rax
    je unwind_stack
    
    #division on combined rax, rdx:
    movq $0,   %rdx #set rdx to 0 (needed)
    div %rbx
    
    #remainer -> stack:
    addq $'0', %rdx #conversion 0->'0'
    pushq %rdx
    incq %rcx
    
    #result is already in rax, so next iteration
    jmp put_next_char_onto_stack
    
    

unwind_stack: 
    #remember result in %rax
    movq %rcx, %rax 
    
#corner case: number=0    
    cmpq $0, %rcx
    jne unwind_loop
    
    movb $'0', (%rsi)
    incq %rsi
    movq $1, %rax # length is 1!
    jmp footer
      
#normal case:
unwind_loop:   
    cmpq $0, %rcx
    je footer    
    
    popq %rbx
    movb %bl, (%rsi)
    incq %rsi
    decq %rcx
     
    jmp unwind_loop
    
    
footer:
   # 1) rax is already set
   # 2) add \0 to string:
    movb $0, (%rsi)
    incq %rsi
    retq
    
