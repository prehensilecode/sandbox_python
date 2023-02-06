#!/usr/bin/env python3
# https://www.includehelp.com/python/pandas-sort-by-group-aggregate-and-column.aspx

import pandas as pd

# Creating DataFrame
df = pd.read_csv('data.csv')

# convert Duration from timedelta to seconds
df['Duration'] = df['Duration'].apply(lambda x: pd.to_timedelta(x).total_seconds())
df = df.astype({'Ncpus': 'float', 'Mem': 'float'})
print(df)

print()

print('Group by "Account" + "Partition", and sum')
print(df.groupby(['Account', 'Partition']).sum())

print()
MAXCPU=48.
MAXMEM=65536.
MAXBMMEM=1572864.

df['CPUseconds'] = df.apply(lambda row: row.Ncpus * row.Duration, axis=1)
df['Memseconds'] = df.apply(lambda row: row.Mem * row.Duration, axis=1)
df['Fracmem'] = df.apply(lambda row: row.Mem/MAXMEM, axis=1)
df['Fracnode'] = df.apply(lambda row: max(float(row.Ncpus)/MAXCPU, row.Mem/MAXMEM), axis='columns')
df['Nodeseconds'] = df.apply(lambda row: row.Duration * max(row.Fracnode, row.Fracmem), axis='columns')

# Display Original DataFrames
print("Created DataFrame: \n",df,"\n")
print()

# Groupby
print('Grouped by Account and Partition')
df_agg = df[['Account', 'Partition', 'Nodeseconds']].groupby(['Account', 'Partition']).agg({'Nodeseconds':sum})
print(df_agg)
print()

print('By Account and TotalNodeseconds')
df['TotalNodeseconds'] = df.groupby('Account')['Nodeseconds'].transform(sum)
print(df[['Account', 'TotalNodeseconds']].drop_duplicates().sort_values(by=['TotalNodeseconds'], ascending=False))
print()

# Sorting by TotalNodeseconds
#new_index = df.sort_values(['TotalNodeseconds', 'Account', 'Partition'], ascending=[False, True, True]).drop('TotalNodeseconds', axis=1)[['Account', 'Partition']]
#
#print('new_index = ')
#print(new_index)
#print()

