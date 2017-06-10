import sys

from RMState import RMState as State

def trace_state(rmstate):
        print >> sys.stderr, "rmstate was: "
        print >> sys.stderr, "\t\trmstate.b:", rmstate.b
        print >> sys.stderr, "\t\trmstate.acc:", rmstate.acc
        print >> sys.stderr, "\t\trmstate.REGS:", rmstate.REGS
        print >> sys.stderr, "\t\trmstate.ended:", rmstate.ended


def interpret(initialRegisterValues, parsed_lines, trace_on = False):
    rmstate=State(initialRegisterValues)
    if trace_on:
        print >> sys.stderr, "Initial state"
        trace_state(rmstate)

    step=1
    while not rmstate.ended:
        try:
            parsed_lines[rmstate.b-1].interpret(rmstate)
            rmstate.b+=1
        except Exception as e:
            print >> sys.stderr, "Runtime error encountered: [", str(e), "] during step", step
            print >> sys.stderr, "rmstate was: "
            print >> sys.stderr, "\t\trmstate.b:", rmstate.b
            print >> sys.stderr, "\t\trmstate.acc:", rmstate.acc
            print >> sys.stderr, "\t\trmstate.REGS:", rmstate.REGS
            print >> sys.stderr, "\t\trmstate.ended:", rmstate.ended
            exit(1)
        if trace_on:
            print >> sys.stderr, "After step", step
            trace_state(rmstate)
        step+=1

    return rmstate.REGS[0]
