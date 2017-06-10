#stores the current state of the register machine for the interpreter

class RMState:
    def __init__(self, REGS):
        self.b = 1
        self.acc = 0
        self.REGS = REGS
        self.ended = False
