#!/usr/bin/env python3
import sys
import os
import pandas as pd

df = pd.DataFrame({"A": ['foobarPrj', 'doePrj', 'hello123Prj'], "B": ['foobarPrj', 'doePrj', 'hello123Prj']})

print(df)
print('')

print('replace inplace')
#df.A.replace({r'^([a-z0-9]+)Prj$': r'\1'}, regex=True, inplace=True)
df['A'].replace({r'^([a-z0-9]+)Prj$': r'\1'}, regex=True, inplace=True)

df['A'] = df['A'].str.capitalize()

print(df)
print('')


df['C'] = df['B']
df.replace(to_replace={'C': 'foobarPrj'}, value={'C': 'funded'}, inplace=True)

print('replace using "to_replace" and "value"')
print(df)
print('')

