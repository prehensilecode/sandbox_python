#!/usr/bin/env python3
import delorean
import fiscalyear
import datetime

start_date = datetime.datetime.fromisoformat('2021-07-01')
print(f'start_date = {start_date}')
end_date = datetime.datetime.fromisoformat('2022-02-28')
print(f'end_date = {end_date}')

for stop in delorean.stops(freq=delorean.MONTHLY, timezone='US/Eastern', start=start_date, stop=end_date):
    print(stop)

fiscalyear.setup_fiscal_calendar(start_month=7)
drexel_fy = fiscalyear.FiscalYear(2022)
print(drexel_fy)
print(drexel_fy.start.year)
print(drexel_fy.start.month)
print(drexel_fy.start.day)
print(type(drexel_fy.start.day))

drexel_start_date = f'{drexel_fy.start.year}-{drexel_fy.start.month:02d}-{drexel_fy.start.day:02d}'
print(drexel_start_date)

sd = datetime.datetime.fromisoformat(drexel_start_date)
print(f'sd = {sd}')

ed = datetime.datetime.fromisoformat('2022-03-01')

dt = datetime.timedelta(days=1)
ed = ed - dt
print(f'ed = {ed}')

for stop in delorean.stops(freq=delorean.MONTHLY, timezone='US/Eastern', start=sd, stop=ed):
    print(f'{stop.date.year}-{stop.date.month:02d}')
