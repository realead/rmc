# error codes returned by the executable

#could not parse command line arguments, wrong arguments
.equ ERROR_WRONG_CHAR, 2

#overflow during the runtime setup
.equ ERROR_OVERFLOW, 3

#wrong number of arguments
.equ ERROR_NO_N_REG, 4

#more than 0 cells needed
.equ ERROR_ZERO_CELLS, 5

#there are more initial values, than cells
.equ ERROR_TOO_MANY_ARGUMENTS, 6
