#!/usr/bin/env python3.6
import sys
import os
import pathlib

p = pathlib.Path('..')

for x in list(p.glob('*.py')):
    print(x)

print('- - - - - - - - - - - - - - - - - - -')

for y in list(p.glob('**/*.py')):
    print(y)

print('- - - - - - - - - - - - - - - - - - -')

for z in p.glob('*.py'):
    print(z)
    print(type(z))

pathlist = []
p = pathlib.Path('/mnt/HA/sysadmin/RCM/2018-03')
for x in p.iterdir():
    pathlist.append(x)

print(pathlist)
print('. . . . .')
print(sorted(pathlist))

