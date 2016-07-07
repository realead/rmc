
class RMCError(Exception):
    pass
    
    
#operations throws RMCError if not successful


#throws also for +1, +2 and so on (but also -1)
def asNonnegInt(literal, must_be_positive=False, lit_name="unknown"):
    condition="positive" if must_be_positive else "nonnegative"
    if not literal.isdigit():
        raise RMCError(lit_name+" must be a "+condition+" integer, found "+literal)
    res=int(literal)
    if must_be_positive and res==0:
        raise RMCError(lit_name+" must be a "+condition+" integer, found "+literal) 
    return res   
