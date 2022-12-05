#!/usr/bin/env python3
import sys, os
import pandas as pd

data = [{'a': 1, 'b': 16}, {'a': 2, 'b': 17}, {'a': 3, 'b': 18}, {'a': 19, 'b': 4}, {'a': 20, 'b': 5}]

df = pd.DataFrame(data)

print(df)
print()

# add new column
df['c'] = df.apply(lambda x: max(x.a, x.b), axis=1)

print(df)