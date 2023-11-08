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
print(everyone_df.describe())
print(everyone_df.head(13))
print()
print(everyone_df[240:266])
