#!/usr/bin/env python3
import sys
import os
import time
import datetime
import delorean
import dateutil

dd = 18344

proposed_exp_str = '2021/6/14'
proposed_exp = delorean.parse(proposed_exp_str)
print('proposed_exp = ', proposed_exp)

exp = delorean.epoch(0) + datetime.timedelta(days=dd)
print('exp = ', exp)
print('exp.datetime = ', exp.datetime)
dts = dateutil.parser.parse(str(exp.datetime))
print('dts.date() = ', dts.date())
print('delorean.Delorean(dts) = ', delorean.Delorean(dts))

if delorean.Delorean(dts) > proposed_exp:
    print('proposed_exp is later than existing')
else:
    print('proposed_exp is earlier than existing')
