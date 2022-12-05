#!/usr/bin/env python3
import sys
import os
import pandas as pd

data_list = ['123456', '123456.0', '123456.1', '123456.10']

df = pd.DataFrame(data_list, columns=['JobID'])

print(df)
print()
print(f'pattern is r"\d+\.\d+"')
print(df['JobID'].str.contains(r'\d+\.\d+'))

