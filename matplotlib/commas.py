#!/opt/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df = pd.DataFrame({'A': ['A', 'B'], 'B': [1000,2000]})

fig, ax = plt.subplots(1, 1, figsize=(2, 2))
df.plot(kind='bar', x='A', y='B',
        align='center', width=.5, edgecolor='none', 
        color='grey', ax=ax)

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
plt.xticks(rotation=25)

plt.show()
