#!/usr/bin/env python3
import sys
import os
import numpy as np
import pandas as pd

a_list = ['1-12:00:28', '1 days 12:00:28', '23:14:49']
a_df = pd.DataFrame(a_list, columns=['Elapsed'])

print(a_df)
print('')
print(a_df.dtypes)
print('')

a_df['Elapsed'].replace({r'\-', ' days '}, regex=True, inplace=True)

print(a_df)
print('')

a_df.loc[:, 'Elapsed'] = pd.to_timedelta(a_df['Elapsed'])

print(a_df)
print('')


