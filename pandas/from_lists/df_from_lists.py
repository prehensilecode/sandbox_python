#!/usr/bin/env python3
import pandas as pd

rows = [['tom', 25],
        ['dick', 32],
        ['harry', 12]]

headers = ['Name', 'Age']

df = pd.DataFrame(rows, columns=headers)
print(df)


