#!/usr/bin/env python3
import sys
import os
import numpy as np
import pandas as pd
import datetime

dt = datetime.timedelta(days=1)
a_list = ['1-12:00:28', '1 days 12:00:28', '23:14:49']
b_list = [datetime.datetime.now(), datetime.datetime.now() + dt, datetime.datetime.now() + dt*2]

print(a_list)
print(b_list)

a_df = pd.DataFrame(
        {'When': b_list,
         'Elapsed': a_list
        })

print(a_df)
print('')
print(a_df.dtypes)
print('')

a_df['Elapsed'].replace(to_replace=r'\-', value=' days ',
                        regex=True, inplace=True)

print(a_df)
print('')

a_df.loc[:, 'Elapsed'] = pd.to_timedelta(a_df['Elapsed'])

print(a_df)
print('')

a_df.to_json('a.json', date_format='epoch')


