#!/usr/bin/env python3
# https://www.statology.org/seaborn-stacked-bar-plot/
# https://www.python-graph-gallery.com/stacked-and-percent-stacked-barplot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
morning = [44, 46, 49, 59, 54]
evening = [33, 46, 50, 49, 60]

df = pd.DataFrame({'Day': day, 'Morning': morning, 'Evening': evening})

print('df = ')
print(df)

sns.set(style='white')
sns.color_palette('muted')

df.set_index('Day').plot(kind='bar', stacked=True)
plt.savefig('tempchart1.png')
plt.clf()

# create 2 charts and stack them
# first, get total height of bar

df['Total'] = df['Morning'] + df['Evening']
print('df = ')
print(df)

# chart 1 (top) - evening
bar1 = sns.barplot(x='Day', y='Total', data=df, color='darkblue')

# chart 2 (bottom) - morning
bar2 = sns.barplot(x='Day', y='Morning', data=df, color='lightblue')

# legend
top_bar = mpatches.Patch(color='darkblue', label='Evening')
bottom_bar = mpatches.Patch(color='lightblue', label='Morning')
plt.legend(handles=[top_bar, bottom_bar])
plt.savefig('tempchart2.png')
plt.clf()

# horizontal
bar1 = sns.barplot(x='Total', y='Day', data=df, color='darkblue')
bar2 = sns.barplot(x='Morning', y='Day', data=df, color='lightblue')
right_bar = mpatches.Patch(color='darkblue', label='Evening')
left_bar = mpatches.Patch(color='lightblue', label='Morning')
plt.title('FOO BAR')
plt.legend(handles=[right_bar, left_bar])
plt.savefig('tempchart3.png')
plt.clf()
