#!/usr/bin/env python3
import sys
import os
import delorean
import datetime
import pandas as pd
import numpy as np

adf = pd.read_csv('alldata.csv')

print(adf)

print(adf[['Index', 'Glyph']])

print(type(adf[['Index', 'Glyph']]))

adf[['Index', 'Glyph']].to_csv('foo.csv')
