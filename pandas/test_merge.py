#!/usr/bin/env python3
import sys, os
import pandas as pd

adf = pd.DataFrame.from_csv('alldata.csv')
idf = pd.read_csv('ofinterest.csv')

print("adf:")
print(adf.describe())
print("")
print(adf.head(5))

print("")

print("idf:")
print(idf.describe())
print("")
print(idf)

merge_df = adf.merge(idf, on=['Name', 'Name'])

print("")
print("merge_df:")
print(merge_df.describe())
print("")
print(merge_df)

