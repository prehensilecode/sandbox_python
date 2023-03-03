#!/usr/bin/env python3.10
import sys
import os
import pandas as pd
import numpy as np

headers = ['A', 'B', 'C']
data = [['001', '002', '123'],
        ['010', '020', '456'],
        [np.NaN, '200', '789']]

df = pd.DataFrame(data, columns=headers)

print(df)
print()

df['A'] = df['A'].astype('string')

print(df)
print()

df.to_csv('foo.csv', index=False)

