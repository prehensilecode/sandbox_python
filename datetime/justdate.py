#!/usr/bin/env python3
import sys
import os
import datetime
import delorean


today = datetime.date.today()
print(f'type(today) = {type(today)}')
print(f'today = {today}')
print(f'today.year = {today.year}')
print(f'today.month = {today.month}')
print(f'today.day = {today.day}')

print()

foo_date = datetime.date(year=2022, month=4, day=21)
print(f'type(foo_date) = {type(foo_date)}')
print(f'foo_date = {foo_date}')
print(f'foo_date.year = {foo_date.year}')
print(f'foo_date.month = {foo_date.month}')
print(f'foo_date.day = {foo_date.day}')

print()

print('Delorean parse 2022-04-21')
try:
    bar_date = delorean.parse('2022-04-21', timezone='US/Eastern')
    print(f'bar_date = {bar_date.date}')
except delorean.exceptions.DeloreanError as e:
    print(f'ERROR: {e}')
    sys.exit(1)

print()

now = delorean.Delorean(timezone='UTC')
print(f'now = {now.datetime}')
print(f'now = {now.datetime.strftime("%Y-%m-%d %H:%M:%S %Z")}')

