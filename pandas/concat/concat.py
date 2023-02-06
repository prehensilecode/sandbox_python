#!/usr/bin/env python3
import sys
import os
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randint(25, size=(4, 4)),
                   index=["1", "2", "3", "4"],
                   columns=["A", "B", "C", "D"])

df2 = pd.DataFrame(np.random.randint(25, size=(6, 4)),
                   index=["5", "6", "7", "8", "9", "10"],
                   columns=["A", "B", "C", "D"])

df3 = pd.DataFrame(np.random.randint(25, size=(4, 4)),
                   columns=["A", "B", "C", "D"])

df4 = pd.DataFrame(np.random.randint(25, size=(4, 4)),
                   columns=["E", "F", "G", "H"])

print('df1 =')
print(df1)
print()

print('df2 =')
print(df2)
print()

print('df3 =')
print(df3)
print()

print('df4 =')
print(df4)
print()

print('pd.concat([df1, df2], axis=0)')
print(pd.concat([df1, df2], axis=0))
print()

print('pd.concat([df3, df4], axis=1)')
print(pd.concat([df3, df4], axis=1))
print()
