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

ind = df.loc[df['username'] == 'ddd'].index
print(ind)
print(df.loc[ind])
