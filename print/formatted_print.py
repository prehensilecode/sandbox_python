#!/usr/bin/env python3
import sys

firstnames = ['John', 'Andrew']
lastnames = ['Smith', 'Lloyd Weber']
surnames = []
commonnames = []

names = zip(firstnames, lastnames)
for n in names:
    surname = '\ '.join(n[1].split())
    commonnames.append('''{}\ {}'''.format('\ '.join(n[0].split()), surname))

print(commonnames)
