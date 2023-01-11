#!/usr/bin/env python3
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('data.csv')
df['Duration'] = df['Duration'].apply(lambda x: pd.to_timedelta(x).total_seconds())
print(df)

print()

print('Group by "Account" + "Partition", and sum')
print(df.groupby(['Account', 'Partition']).sum())

print()

df['CPU-seconds'] = df.apply(lambda row: row.Ncpus * row.Duration, axis=1)
print(df)

print()

print('Group by "Account" + "Partition", and sum')
print(df.groupby(['Account', 'Partition']).sum())

print()

print('Multi index')
multi_index = pd.MultiIndex.from_frame(df)
print(multi_index)
