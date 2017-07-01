# rmc

A framework for register machine language.

### Preliminaries

  1. This repository has submodules (`exetest`), so clone it via `git clone --recursive` or if already cloned, get the submodules via a. `git submodule init` + `git submodule update`.
  2. python2.7
  3. gcc is needed for `rmc`, but not `rmi`.

### About

This framework consists of
   1. compiler `rmc.py`. RMC is a register machine compiler, i.e. it compiles register machine code. Right now, the only supported target is **x86_64 linux architecture**.
   2. interpreter `rmi.py`. The interpreter RMI can be used on any operating system with python. 
   3. jit-compiler `rmjit.py`. Right now, the only supported target is **x86_64 linux architecture**.

The syntax and model of the register machine is closely related to the register machine described in *Alexander Asteroth, Christel Baier, Theoretische Informatik, Eine Einführung in Berechenbarkeit, Komplexität
und formale Sprachen mit 101 Beispielen*.

#### Memory model:
   1. There is an arbitrary number **n** of 64bit registers with indices **0** to **n-1**, inclusive. A register can contain any positive integer from the range [0, 2^64-1].
   2. The register machine possesses a command counter *b* and a 64bit accumulator *acc* which is resposible for calculations.
   3. At the start of the program, *b=1* and *acc=0* holds.
   
#### Syntax:
   Every line has to start with its number. The first line has the number 1, the second - 2, the third - 3 and so on. Than the operation and its operands follows on the same line.
   Comments are yet to be implemented.
   
#### Operations:

1. **LOAD** loads a value into the accumulator, the values of the in this operation participating registers stay unchanged. The value *b* gets incremented by 1.
    * LOAD #k - acc=k, loads the const value k into the accumulator. k>=0. 
    * LOAD k  - acc=reg[k], loads the value of the k-th register into the accumulator. k>=0
    * LOAD *k - acc=reg[reg[k]], loads the value of the m-th register, with m being the value in the k-th register. k>=0

2. **STORE** stores the value of the accumulator into a register, the value of the accumulator stays unchanged.  The value *b* gets incremented by 1.
    * STORE k - reg[k]=acc, stores the accumulator into the k-th register, k>=0
    * STORE *k - reg[reg[k]]=acc, stores the accumulator value to the m-th register, with m being the value in the k-th register. k>=0
    * Note STORE #k is not a valid expression
3. **ADD** adds a value to the accumulator, the values of the in this operation participating registers stay unchanged. The value *b* gets incremented by 1.
    * ADD #k  - acc+=k, adds the value k to the accumulator. k>=0
    * LOAD k  - acc+=reg[k], adds the value of the k-th register to the accumulator. k>=0
    * LOAD *k - acc+=reg[reg[k]], adds the value of the m-th register, with m being the value in the k-th register. k>=0
4. **SUB** subtracts a value from the accumulator, the values of the in this operation participating registers stay unchanged. The value *b* gets incremented by 1.
    * SUB #k  - acc=max(0, acc-k), subtracts the value k from the accumulator. k>=0. If acc was smaller than k, result is 0.
    * SUB k  - acc=max(0, acc-reg[k]), subtracts the value of the k-th register to the accumulator. k>=0. If acc was smaller than reg[k], result is 0.
    * SUB *k - acc+=max(0, acc-reg[reg[k]]), subtracts the value of the m-th register, with m being the value in the k-th register. k>=0. If acc was smaller than reg[m], result is 0.   
5. **MULT** multiplies the accumulator with the value, the values of the in this operation participating registers stay unchanged. The value *b* gets incremented by 1.
    * MULT #k  - acc*=k, multiplies the accumulator with the value k. k>=0. 
    * MULT k  - acc*=reg[k], multiplies the accumulator with the value of the k-th register. k>=0.
    * MULT *k - acc*=reg[reg[k]], multiplies the accumulator with the value of the m-th register, with m being the value in the k-th register. k>=0. If acc was smaller than reg[m], result is 0.     
6. **DIV** integer division of the accumulator with the value, the values of the in this operation participating registers stay unchanged. Program crashes if the divisor is 0. The value *b* gets incremented by 1.
    * DIV #k  - acc\=k, divides the accumulator through the value k. k>=0. 
    * DIV k  - acc\=reg[k], divides the accumulator through the value of the k-th register. k>=0.
    * DIV *k - acc\=reg[reg[k]], divides the accumulator through the value of the m-th register, with m being the value in the k-th register. k>=0. If acc was smaller than reg[m], result is 0.
7. **END**  no operands, ends the program. In every program the must be exactly one commend END.
8. **GOTO** unconditional jump, changes the program flow.
    * DIV #k - sets b=k, this means the line k will be executed in the next step.
9. **JZERO** conditional jump, jumps if the accumulator is 0 or proceedes with the next line otherwise.
    * JZERO #k -  set b=k if accumulator is 0, otherwise b=b+1.
     
### Usage 

#### rcm (compiler)

*gcc* and *python2.7* are necessary . gcc is used to assemble and link assembler code generated by rmc. 

   1. run `python2.7 rmc.py -c code.rm -o program` for compiling your register machine code
   2. run your executable with `./program X Val0 Val1 Val2 ...*`

##### ABI
   At the start of the program the user must define the number of the registers and the initial values of the registers (every one of them [0..2^64-1]). The default initial value is 0. The inital value of the accumulator is 0, of the b counter - 1.
   A possible start up could look as follows:
   
    my_prog 7 2 4
   
   would means the program *my_prog* can use 7 registers with initial values `[2,4,0,0,0,0,0]`.
   The result of the calculation must be stored in register 0 - this value will be printed if program terminates normally.


#### rmi (interpreter)

  1. run `python2.7 rmi.py -f code.rm -n 7 -i "2 4"` for interpreting the program `code.rm`, the option `-n` reserves the registers for the program (in this case 7), the option `-i` sets the initial values of these reserved register, in this case `[2,4,0,0,0,0,0]` (if not explicitly stated, registers are initialized to 0).

#### rmjit (jit-compiler)

  1. run `python2.7 rmjit.py -f code.rm -n 7 -i "2 4"` for interpreting the program `code.rm`, the option `-n` reserves the registers for the program (in this case 7), the option `-i` sets the initial values of these reserved register, in this case `[2,4,0,0,0,0,0]` (if not explicitly stated, registers are initialized to 0).
   
### Example

The following program *max.rm* returns the maximum of two arguments:

    1 LOAD 1
    2 SUB 0
    3 JZERO #6
    4 LOAD 1
    5 STORE 0
    6 END

It loads the value of the second (0-based!) register into the accumulator and subtracts the first value. If the result is 0, than the first value was at least as big as the second, there is nothing to do, so we jump to the end. Otherwise the second element is the maximum, so we copy it into the first register.

After building it with `python2.7 rmc.py -c max.rm -o my_max`, we can run the resulting *my_max* executable:
   1. `./my_max 2 100 99` means: the program uses two registers and they are initialized with 100 and 99. It prints 100 - the maximum of the two values to the stdout.
   2. `./my_max 5 100 101` says: the program uses at most 5 registers. It prints 101 as answer.
    
Other examples can be seen in folder *tests*. 
   1. Run `sh unit_test.sh` for running all tests
   2. Run `sh unit_test.sh rmc` for running only for `rmc.py`
   3. Run `sh unit_test.sh rmi` for running only for `rmi.py`
   3. Run `sh unit_test.sh rmjit` for running only for `rmjit.py`
   4. Run `sh unit_test.sh rmi XXX` for running only tests for `rmi.py` from the test-subfolder `XXX` 
   5. Run `sh unit_test.sh all . --keep` for running all tests and keeping temporary files (results of `rmc.py`-run)

### Times

For comparison on your system, run `sh time_test.sh` in the *tests/time_test*  folder. On my system `rmjit` is about `3%` slower than `rmc` compiled code and about `200` times faster than the intepreter `rmi`.
 
### How rmc works    
Similar to C-runtime, there is a Register Machine runtime - boilerplate code which interprets the command line arguments and sets the initial values of the registers. After the preparation the runtime calls rmprogram - a function written by the rm-compiler. 

For the building of the executable the generated assembler code is compiled using *gas*. Right now, the rm-runtime is not prebuild and is compiled with every run of `rmc.py`. Use flag -v to see all issued commands.

### (Possible Future)

   1. Comments

