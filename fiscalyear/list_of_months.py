#!/usr/bin/env python3.9
import sys, os
import fiscalyear as fy
import datetime

today = datetime.date.today()
print(f'today = {today}')

fy.setup_fiscal_calendar(start_month=7)

a = fy.FiscalYear(today.year)
print(f'FY a = {a}')
print(f'FY a.start = {a.start}')
print(f'FY a.end = {a.end}')
