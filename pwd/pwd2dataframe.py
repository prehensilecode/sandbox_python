#!/usr/bin/env python3
import sys
import os
import pwd
import grp
import pandas as pd

# from https://stackoverflow.com/a/11531402/299952

def filter(everyone_df):
    ret_df = everyone_df[~everyone_df['pw_gecos'].str.contains(r'\!disabled')]
    print('ret_df.describe():')
    print(ret_df.describe())
    print()

    ret_df = ret_df[~ret_df['pw_gecos'].str.contains(r'^pseudo\ user')]
    print('ret_df.describe():')
    print(ret_df.describe())
    print()

    ret_df = ret_df.loc[(ret_df['pw_uid'] > 10000) &
                        (ret_df['pw_gid'] > 1024) &
                        (ret_df['pw_name'] != 'nfsnobody')]

    return ret_df


everyone = pwd.getpwall()

print(type(everyone[75]))
print(everyone[75])

data = [{attr: getattr(p, attr) for attr in dir(p) if attr.startswith('pw_')} for p in everyone]
everyone_df = pd.DataFrame(data)
print()
print('everyone_df.describe():')
print(everyone_df.describe())
print()

print(everyone_df.head(13))
print()

print(everyone_df[240:266])
print()


print('everyone_df.describe():')
print(everyone_df.describe())

active_users_df = filter(everyone_df)

print()
print('Active users:')
print(active_users_df.describe())
print()
print(active_users_df.head(20))
print()

active_users_df.to_csv('active_users.csv', index=False)
