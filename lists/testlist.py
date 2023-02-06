#!/usr/bin/env python3
import sys
import os

def dosomething(lst):
    print('dosomething:')
    for i in lst:
        print(i)


foo = [1, 2, 3]
bar = []

print(f'foo = {foo}')
dosomething(foo)
print()

print(f'bar = {bar}')
dosomething(bar)
print()
