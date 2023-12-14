#!/usr/bin/env python3
import sys
import os
import re

gecos = "Albert Einstein <Albert.Einstein@advstud.princeton.edu>, RC=1 PI = einstein (some other comment, and maybe more), Created: 1921-04-02 (special guest)"

name_email_pat = re.compile(r'(.*)\ +<(.*)>')

gecos_split = gecos.split(',')
print(gecos_split)
print()

m = name_email_pat.match(gecos_split[0].strip())
print(m.group(0))
print(f'Full name = {m.group(1)}')
print(f'Email = {m.group(2)}')

#rc_pat = re.compile(r'^RC=(\d)')
#m = rc_pat.match(gecos_split[1].strip())
#rc = int(m.group(1))
#print(f'RC = {rc}')

#print(f'gecos_split[1] = {gecos_split[1]}')
#pi_pat = re.compile(r'PI\s=\s(\w+)\s')
#m = pi_pat.match(gecos_split[2].strip())
#print(f'm = {m}')
#pi = m.group(1)
#print(f'PI = {pi}')

rc_pi_pat = re.compile(r'^RC=(\d+)\s+PI\s+=\s+(\w+)\s+.*')
print(f'rc_pi_pat = {rc_pi_pat}')
m = rc_pi_pat.match(gecos_split[1].strip())
print(f'm = {m}')
rc = int(m.group(1))
pi = m.group(2)
print(f'RC = {rc}')
print(f'PI = {pi}')
