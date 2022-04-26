#!/usr/bin/env python3
import pandas as pd

df = pd.DataFrame({"Data": ['source=book', 'source=book', 'source=journal'], "Data2": ['social-media=facebook', 'social-media=instagram', 'social-media=facebook']})

print(df['Data'].apply(lambda x : x.split('=')[-1]))
print(df['Data2'].apply(lambda x : x.split('=')[-1]))
