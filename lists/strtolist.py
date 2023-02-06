#!/usr/bin/env python3
import sys
import os

foo = '[10, 11, 12, 2]'

intlist = [int(f) for f in foo[1:-1].split(',')]

print(intlist)

