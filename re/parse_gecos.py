#!/usr/bin/env python3
import sys
import os
import re

gecos = "Albert Einstein <Albert.Einstein@advstud.princeton.edu>, RC=1, PI = einstein, Created: 1921-04-02 (special guest)"

name_email_pat = re.compile(r'(.*)\ +<(.*)>')

gecos_split = gecos.split(',')
print(gecos_split)
print()

m = name_email_pat.match(gecos_split[0].strip())
print(m.group(0))
print(f'Full name = {m.group(1)}')
print(f'Email = {m.group(2)}')

rc = int(gecos_split[1].split('=')[1].strip())
print(f'RC = {rc}')

pi = gecos_split[2].split('=')[1].strip()
print(f'PI = {pi}')
