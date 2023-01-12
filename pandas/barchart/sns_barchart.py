#!/usr/bin/env python3
import sys
import pandas as pd

speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ['snail', 'pig', 'elephant', 'rabbit', 'giraffe', 'coyote', 'horse']

df = pd.DataFrame({'speed': speed, 'lifespan': lifespan}, index=index)

print(df)

ax = df.plot.bar(rot=0)

ax.figure.savefig('chart.png')

ax = df.plot.bar(stacked=True)

ax.figure.savefig('chart_stacked.png')

