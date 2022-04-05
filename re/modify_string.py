#!/usr/bin/env python3
import sys
import os
import re


grpPat = re.compile(r"Grp$")

groups = ['fooGrp', 'barGrp', 'bazGrp']

for g in groups:
    print(grpPat.sub('Prj', g))
