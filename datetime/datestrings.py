#!/usr/bin/env python3
import sys, os, datetime
import delorean

d = datetime.date(year=2018, month=4, day=21)
print(d)
print(type(d.strftime('%Y-%m-%d')))
print(d.strftime('%Y-%m-%d'))

print()

d = datetime.date(year=2021, month=4, day=1)
print(d.strftime('%B %Y'))

print()

d = delorean.Delorean(timezone='US/Eastern')
print(f'd = {d.datetime}')

