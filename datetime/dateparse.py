#!/usr/bin/env python3
import sys
import os
import delorean

datestr = "2020-12-03"
print("datestr = {}".format(datestr))
foo = delorean.parse(datestr, dayfirst=False)
print("dayfirst = False")
print(foo.datetime.isoformat())
bar = delorean.parse(datestr, dayfirst=True)
print("dayfirst = True")
print(bar.datetime.isoformat())
print("")

datestr = "2020-01-09"
print("datestr = {}".format(datestr))
foo = delorean.parse(datestr, dayfirst=False)
print("dayfirst = False")
print(foo.datetime.isoformat())
bar = delorean.parse(datestr, dayfirst=True)
print("dayfirst = True")
print(bar.datetime.isoformat())
print("")


datestr = "2020-12"
print("datestr = {}".format(datestr))
foo = delorean.parse(datestr, dayfirst=False)
print("dayfirst = False")
print(foo.datetime.isoformat())
bar = delorean.parse(datestr, dayfirst=True)
print("dayfirst = True")
print(bar.datetime.isoformat())
print("")

datestr = "2020-01"
print("datestr = {}".format(datestr))
foo = delorean.parse(datestr, dayfirst=False)
print("dayfirst = False")
print(foo.datetime.isoformat())
bar = delorean.parse(datestr, dayfirst=True)
print("dayfirst = True")
print(bar.datetime.isoformat())
print("")

for m in range(1,13):
    datestr = "2019-{}-1".format(m)
    print(delorean.parse(datestr, dayfirst=False).datetime.isoformat())
print("")

