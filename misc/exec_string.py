#!/usr/bin/env python3

def op(opstr, value):
    old = value
    lcls = locals()
    exec(opstr, globals(), lcls)
    new = lcls['new']

    return new


instr = "new = old + 5"
print(op(instr, 20))

instr = "new = old * old"
print(op(instr, 20))

instr = "new = old * 1.5"
print(op(instr, 20))
