#!/usr/bin/env python3
import sys
import os
import pandas as pd

df = pd.DataFrame({
    'username': ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],
    'fullname': ['Alice Anderson', 'Bob Bridger', 'Chris Compton', 'Daniel Dumbarton', 'Eric Ericsson', 'Fanny Foster']
    })

print('df =')
print(df)
print()

ind = df.loc[df['username'] == 'ddd'].index
print('ind =')
print(ind)
print()
print('df.loc[ind] =')
print(df.loc[ind])
print()
print('type(df.loc[ind]) = ')
print(type(df.loc[ind]))
print()
print(df.loc[ind][['fullname']])
print()
print(type(df.loc[ind][['fullname']].values[0]))
print()

print(df[df['username'] == 'ddd']['fullname'].values[0])
