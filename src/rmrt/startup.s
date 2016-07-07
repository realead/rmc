#handles the command line arguments and set ups 
#the register machine.
#
#the call of rm-program
#
#rmprogram 100 2 3 4 5
#
#means register machine has 100 registers and R0=2, R1=3, R2=4, R3=5 and all others 0 at the start of the program
#
#calls program, which is the comiled rm-program
#
#after the end of the program, prints out the result (which is saved in register 0)
#and shuts down
#
#register are on the stack:
# R0 -> 0(%rbp)
# R1 -> 8(%rbp) 
# R2 -> 16(%rbp) and so on
#

#Attention: no error handling yet!

.include "linux64.h"
.include "error_codes.h"

.section .data
    .globl REGS
REGS:    
    .quad 0
.section .bss
    .equ BUFFER_SIZE, 500
    .lcomm OUTPUT_BUFFER, BUFFER_SIZE
    
    
.section .text
    .globl _start
    .equ ST_ARGC, 0
    .equ ST_REG_N, 2*QUAD_SIZE
_start:
    movq %rsp, %rbp

check_n_given:
    cmpq $2, ST_ARGC(%rbp) 
    jl no_n_given
      
    #number of RM-registers is given
    movq ST_REG_N(%rbp), %rdi
    call atouq
    
check_nonzero_n:    
    cmpq $0, %rax
    je zero_cells_error
    
#put 0-initialized values on stack
    addq $2, %rax #because first two arguments are the name of the program and the number of registers, we assume there will be no overflow:)

#check_ini_cnt
    cmpq ST_ARGC(%rbp), %rax
    jl too_many_ini_cells
    
    #keep the number of 0-initialized cells in rax:    
    subq ST_ARGC(%rbp), %rax
    
fill_stack:
    cmp $0, %rax
    je ini_regs
    
    pushq $0
    decq %rax
    jmp fill_stack
   
#put register initialized via command line

ini_regs:
    movq ST_ARGC(%rbp), %rcx
    imulq $QUAD_SIZE, %rcx #offset to the last argument on the stack

ini_loop:    
    cmpq $ST_REG_N, %rcx
    je start_program
    
    pushq %rcx
    movq (%rbp,%rcx), %rdi
    call atouq
    
    popq %rcx
    pushq %rax #the initial value for this register was in %rax
    
    
    subq $QUAD_SIZE, %rcx
    jmp ini_loop
   
    
#everything set up, start the program
start_program:
    #remember the start  of registers
    movq %rsp, REGS
    call rmprogram
    
#print out result:
    # 1) convert to string
    popq %rdi #result should be on the top of the stack
    movq $OUTPUT_BUFFER, %rsi
    call uqtoa
    
    # 2a) print to stdout
    movq  %rax, %rdx              #remember size of the string
    movq  $SYS_WRITE, %rax        #write to
    movq  $STDOUT, %rdi   #to this file
    movq  $OUTPUT_BUFFER, %rsi      #this buffer
                                  #count from %rdx
    syscall
    
    # 2b) print new line to stdout
    movq $STDOUT, %rdi
    call print_newline
#now shout down:
    movq  $SYS_EXIT, %rax
    movq  $0, %rdi
    syscall
    
zero_cells_error:
    movq $ERROR_ZERO_CELLS, %rdi
    call error_exit #there is no comming back  
      
no_n_given:
    movq $ERROR_NO_N_REG, %rdi
    call error_exit #there is no comming back 
    
too_many_ini_cells:
    movq $ERROR_TOO_MANY_ARGUMENTS, %rdi
    call error_exit #there is no comming back 
       
    
