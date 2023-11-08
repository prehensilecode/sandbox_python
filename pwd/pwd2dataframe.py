#!/usr/bin/env python3
import sys
import os
import pwd
import grp
import pandas as pd

# from https://ludic.mataroa.blog/blog/i-accidentally-saved-half-a-million-dollars/

everyone = pwd.getpwall()

print(type(everyone[75]))
print(everyone[75])

data = [{attr: getattr(p, attr) for attr in dir(p) if attr.startswith('pw_')} for p in everyone]
everyone_df = pd.DataFrame(data)
print()
print(everyone_df.describe())

print()
print(everyone_df.head(13))

print()
print(everyone_df[240:266])

print()
print(~everyone_df['pw_gecos'].str.contains(r'!disabled'))
active_users_df = everyone_df[~everyone_df['pw_gecos'].str.contains(r'!disabled')]
active_users_df = everyone_df[~everyone_df['pw_gecos'].str.contains(r'^pseudo\ user')]
active_users_df = active_users_df.loc[(active_users_df['pw_uid'] > 10000) \
        & (active_users_df['pw_gid'] > 1024) \
        & (active_users_df['pw_name'] != 'nfsnobody')]

print()
print('Active users:')
print(active_users_df.describe())
print(active_users_df.head(20))
