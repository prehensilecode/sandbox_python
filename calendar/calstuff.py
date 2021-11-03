#!/usr/bin/env python3
import sys
import os
import datetime
import calendar
import subprocess

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mdays = calendar.monthrange(2021, 10)
print('monthrange returns first day-of-week of month (Monday = 0), and number of days in month')
print(f'mdays for 2021-10 = {mdays}\n   {weekdays[mdays[0]]}, number of days = {mdays[1]}')

print('')
cal_output = subprocess.run(["cal", "10", "2021"], capture_output=True)
print(cal_output.stdout.decode('utf-8'))

