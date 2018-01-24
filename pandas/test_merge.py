#!/usr/bin/env python3
import sys, os
import pandas as pd

# Two data sets:
# * Full set of data in one DF, adf
# * Set of values of "Name" column which we are interested in, idf
# Want to pick only rows of adf which correspond to items in idf

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

