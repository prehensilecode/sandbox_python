#!/usr/bin/env python3
import sys
import os
import delorean
import datetime
import pandas as pd
import numpy as np

start = datetime.datetime(2019, 1, 1)
dates = []
vals = []
i = 0.
for stop in delorean.stops(freq=delorean.MONTHLY, start=start, count=12, timezone='UTC'):
    dates.append(stop.datetime)
    vals.append(i)
    i += 1.

print(dates)
print(vals)

df = pd.DataFrame({'month': dates, 'usage': vals})

print(df)

print(df.dtypes)

mask = df['month'] < datetime.datetime(2019, 7, 1, tzinfo=datetime.timezone.utc)
print(df[mask])
