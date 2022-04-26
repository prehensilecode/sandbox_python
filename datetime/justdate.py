#!/usr/bin/env python
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
