
import ctypes
import mmap
import array

import rmcerrors

def encodeInt32(z):
    if z<-2**31 or z>=2**31:
        raise RMCError("not a 32bit integer")
    z=(z+2**32)%(2**32) #as 32bit unsigned int
    res=''
    for i in xrange(4):
            res+=chr(z%256)
            z/=256;
    return res

# Equivalent to dlopen(NULL) to open the main process; this means the Python
# interpreter, which links the C library in. Alternatively, we could open
# libc.so.6 directly (for Linux).
libc = ctypes.cdll.LoadLibrary(None)

# Grab the mmap foreign function from libc, setting its signature to:
#
#     void *mmap(void *addr, size_t length, int prot, int flags,
#                int fd, off_t offset)
#
# Per the mmap(2) man page.
mmap_function = libc.mmap
mmap_function.restype = ctypes.c_void_p
mmap_function.argtypes = (ctypes.c_void_p, ctypes.c_size_t,
                          ctypes.c_int, ctypes.c_int,
                          ctypes.c_int, ctypes.c_size_t)

def call_as_jit_code(code, registers):
    """expecting the code to be a function with signature void (unsigned long long)"""
    CODE_SIZE = ((len(code)+1023)/1024)*1024

    # Allocate RWX memory with mmap. Using mmap from libc directly rather than
    # Python's mmap module here because the latter returns a special "mmap object"
    # and we just need the raw address of the mapping. However, we will use the
    # PROT_* and MAP_* constants from the mmap module rather than duplicating them.
    code_address = mmap_function(None, CODE_SIZE,
                                 mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC,
                                 mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS,
                                 -1, 0)

    if code_address == -1:
        raise OSError('mmap failed to allocate memory')

    ctypes.memmove(code_address, code, len(code))

    # Declare the type for our JITed function: int (*JitFuncType)(unsigned long long int* ), and cast
    # code_address (which is a void*) to this type so we could just call it.
    JitFuncType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_ulonglong))
    function = ctypes.cast(code_address, JitFuncType)

    #now input data:
    input_registers = (ctypes.c_ulonglong * (len(registers) / 8)).from_buffer(registers)
    return function(input_registers)


def jitcompile(parsed_lines):

    code=[b'\x48\xc7\xc0\x00\x00\x00\x00'] # mov $0, %rax
    

    #first sweep, placeholder for jumps:
    line_start_adresses=[]
    placeholders = {}
    cur_position=len(code[0])
    for line_id, line in enumerate(parsed_lines):
        line_start_adresses.append(cur_position)#there is a sentinel at the end
        #returns code, mat local_index_of_opcode->goal of the jump
        opcode, placeholder=line.as_x86_64_opcode()
        if placeholder is not None:
            #local to global index
            placeholders[placeholder[0]+len(code)]=(line_id, placeholder[1])
        cur_position+=sum([len(x) for x in opcode])
        code.extend(opcode)
    
    #link (replace placeholders with jump widths:
    for code_index, info in placeholders.items():
        diff=line_start_adresses[info[1]-1]-line_start_adresses[info[0]+1]
        code[code_index]=encodeInt32(diff)
    return code


def jitrun(REGS, parsed_lines, dump_file_name=None):
   
   code = jitcompile(parsed_lines)
   

   if dump_file_name is not None:
        with open(dump_file_name, 'wb') as f:
            f.write(''.join(code))

   arr = array.array('L', REGS);
   call_as_jit_code(''.join(code), arr)
   return arr[0]


    

