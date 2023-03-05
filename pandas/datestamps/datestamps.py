#!/usr/bin/env python3.10
import sys
import os
import pandas as pd

headers = ['Name', 'Expiration date']

data    = [['Alice', '2023-02-04'],
           ['Bob', '2025-12-25'],
           ['Charlie', '1985-09-13']]

df = pd.DataFrame(data, columns=headers)

print(df)
print(df.dtypes)
print()

df['Name'] = df['Name'].astype('string')
df['Expiration date'] = pd.to_datetime(df['Expiration date'])

print('After fixing types')
print(df)
print(df.dtypes)
print()
for i in range(3):
    print(f'df["Expiration date"][{i}] = {df["Expiration date"][i].strftime("%B %d, %Y")}')

print('- - - - - - - - - - -')

# add deliberate inconsistency
data    = [['Alice', '2023-02-04'],
           ['Bob', '2025-12-25'],
           ['Charlie', '1985-13-09']]

df = pd.DataFrame(data, columns=headers)

print('Add inconsistent date format')
print(df)
print(df.dtypes)
print()

try:
    df['Name'] = df['Name'].astype('string')
    df['Expiration date'] = pd.to_datetime(df['Expiration date'])
except Exception as exc:
    print(exc)

print('After fixing types')
print(df)
print(df.dtypes)
print()

print('- - - - - - - - - - -')

# all ambiguous
data    = [['Alice', '2023-02-04'],
           ['Bob', '2025-03-08'],
           ['Charlie', '1985-09-09']]

df = pd.DataFrame(data, columns=headers)

print('All ambiguous date format')
print(df)
print(df.dtypes)
print()

df['Name'] = df['Name'].astype('string')
df['Expiration date'] = pd.to_datetime(df['Expiration date'], format='%Y-%m-%d')

print('After fixing types')
print(df)
print(df.dtypes)
print()

print(f'df["Expiration date"] = \n{df["Expiration date"]}')

print()
for i in range(3):
    print(f'df["Expiration date"][{i}] = {df["Expiration date"][i].strftime("%B %d, %Y")}')


print('- - - - - - - - - - -')
df = pd.DataFrame(data, columns=headers)

print('All ambiguous date format, again, but month and day reversed via "format" arg')
print(df)
print(df.dtypes)
print()

df['Name'] = df['Name'].astype('string')
df['Expiration date'] = pd.to_datetime(df['Expiration date'], format='%Y-%d-%m')

print('After fixing types')
print(df)
print(df.dtypes)
print()

print(f'df["Expiration date"] = \n{df["Expiration date"]}')

print()
for i in range(3):
    print(f'df["Expiration date"][{i}] = {df["Expiration date"][i].strftime("%B %d, %Y")}')
