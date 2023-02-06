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
