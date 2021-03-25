#!/usr/bin/env python3
import sys
import os
import time
import datetime
import delorean
import dateutil

# existing expiration (days since epoch)
dd = 19997

exp = delorean.epoch(0) + datetime.timedelta(days=dd)
print('existing exp = ', exp)
print('existing exp.datetime = ', exp.datetime)
dts = dateutil.parser.parse(str(exp.datetime))
print('existing dts.date() = ', dts.date())
print('existing delorean.Delorean(dts) = ', delorean.Delorean(dts))

print('')

proposed_exp_str = '2021/6/14'
proposed_exp = delorean.parse(proposed_exp_str)
print('proposed_exp = ', proposed_exp)

if delorean.Delorean(dts) > proposed_exp:
    print('existing is later than proposed')
else:
    print('existing is earlier than proposed')


print('')

proposed_exp_str = '2031/2/14'
proposed_exp = delorean.parse(proposed_exp_str)
print('proposed_exp = ', proposed_exp)

if delorean.Delorean(dts) > proposed_exp:
    print('existing is later than proposed')
else:
    print('existing is earlier than proposed')
