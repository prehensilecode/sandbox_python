#!/usr/bin/env python3
import sys
import os
import pandas as pd

df = pd.DataFrame({"A": ['foobarPrj', 'doePrj', 'hello123Prj'], "B": ['foobarPrj', 'doePrj', 'hello123Prj']})

print(df)
print('')

df.A.replace({r'^([a-z0-9]+)Prj$': r'\1'}, regex=True, inplace=True)

df['A'] = df['A'].str.capitalize()

print(df)
print('')

