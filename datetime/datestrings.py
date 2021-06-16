#!/usr/bin/env python3
import sys, os, datetime

d = datetime.date(year=2018, month=4, day=21)
print(d)
print(type(d.strftime('%Y-%m-%d')))
print(d.strftime('%Y-%m-%d'))


d = datetime.date(year=2021, month=4, day=1)
print(d.strftime('%B %Y'))

