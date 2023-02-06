#!/usr/bin/env python3
# https://www.includehelp.com/python/pandas-sort-by-group-aggregate-and-column.aspx

import pandas as pd

# Creating a dictionary
d = {
    'A':['Oranges','Bananas','Guavas','Mangoes','Apples'],
    'B':[212.212,3312.3121,1256.3452,2565.565,748.237],
    'C':[False,True,True,False,False]
}

# Creating DataFrame
df = pd.DataFrame(d)

# Display Original DataFrames
print("Created DataFrame: 2\n",df,"\n")

# Grouping by column A by aggregate sum of B
df['result'] = df.groupby('A')['B'].transform(sum)

# Sorting by C
df = df.sort_values(['result','C'], ascending=[True, False]).drop('result', axis=1)

# Display modified DataFrame
print("Modified DataFrame:\n",df)

