#!/usr/bin/env python3.9
import sys, os
import fiscalyear as fy
import datetime
import delorean

today = datetime.date.today()
print(f'today = {today}')

d = delorean.Delorean()
print(f'd = {d} (today)')
print(f'd.last_month() = {d.last_month()}')
print()

fy.setup_fiscal_calendar(start_month=7)

a = fy.FiscalYear(d.datetime.year)
print(f'FY a = {a}')
print(f'FY a.start = {a.start}')
print(f'FY a.end = {a.end}')
print()

b = fy.FiscalYear(2021)
print(f'FY b = {b}')
print(f'FY b.start = {b.start}')
print(f'FY b.end = {b.end}')

c = fy.FiscalMonth(2021, 7)
print(f'Fiscal month c = {c}')
print(f'Fiscal month c.fiscal_month = {c.fiscal_month}')
print(f'Fiscal month c.next_fiscal_month = {c.next_fiscal_month}')
print()

d = fy.FiscalYear(2023)
e = fy.FiscalDate.today()
print(f'FY d = {d}')
print(f'FY d.start = {d.start}')
print(f'FY type(d.start) = {type(d.start)}')
print(f'd.start.__str__() = {d.start.__str__()}')
year, month, day = d.start.__str__().split(' ')[0].split('-')
print(f'year, month, day = {year}, {month}, {day}')
print(f'FY e = {e}')
print(f'FY e.prev_fiscal_month = {e.prev_fiscal_month}')
print()

f = fy.FiscalMonth(2022, 10)
print(f'FY f = {f.fiscal_year}')
print()

start_date = datetime.datetime.fromisoformat(f'{year}-{month}-{day}')
print(f'start_date = {start_date}')
print(f'type(start_date) = {type(start_date)}')

print(f'stops using d')
for stop in delorean.stops(freq=delorean.MONTHLY, timezone='US/Eastern', start=start_date, stop=delorean.Delorean(e.ctime())):
    print(stop)
print()

