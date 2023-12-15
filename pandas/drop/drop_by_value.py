#!/usr/bin/env python3
import sys
import os
import pandas as pd

df = pd.DataFrame({
    'username': ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],
    'fullname': ['Alice Anderson', 'Bob Bridger', 'Chris Compton', 'Daniel Dumbarton', 'Eric Ericsson', 'Fanny Foster']
    })

print(df)
print()

to_drop = ('aaa', 'ccc', 'eee')
ind = df['username'].isin(to_drop)
print(f'ind = \n{ind}\n')
print()
print('df.loc[ind] =')
print()
print(df.loc[ind])
print()
print(df.loc[ind].index)
print()

df.drop(df.loc[ind].index, inplace=True)

print(df)
