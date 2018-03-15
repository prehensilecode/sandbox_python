#!/usr/bin/env python3
import sys, os
from itertools import dropwhile

def memoryPills(pills):
    gen = dropwhile(lambda x: len(x) % 2 != 0, pills)
    next(gen)
    return [next(gen) for _ in range(3)]

pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"]
#pills = ["Med 1", "Med 2", "Med 3", "Med 10", "Med 11", "Med 12", "Med 14", "Med 42", "Med 239"]

gen = dropwhile(lambda x: len(x) % 2 != 0, pills)
next(gen)
print([next(gen) for _ in range(3)])


#foo = memoryPills(pills)
#print(foo)

