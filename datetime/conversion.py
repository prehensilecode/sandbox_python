#!/usr/bin/env python3
import sys
import os
import dateutil
import datetime
import time
import delorean

ms1 = '1470241587717'
ms2 = '1470241584000'
s1  =    '1390316816'

#print("datetime ms1 = ", datetime.datetime(int(ms1)))
#print("datetime ms2 = ", datetime.datetime(int(ms2)))


print(ms1)
print(int(ms1))
sec, msec = divmod(int(ms1), 1000)
print(sec, msec)

print(delorean.epoch(int(sec)).shift('US/Eastern'))
print(delorean.epoch(int(s1)).shift('US/Eastern'))

