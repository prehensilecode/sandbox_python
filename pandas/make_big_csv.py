#!/usr/bin/env python
import sys
import os
import csv
import numpy as np

with open('data.csv', 'w') as csvfile:
    fieldnames = ['mass', 'length']
    data = np.random.rand(100000, 2)
    spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    spamwriter.writeheader()
    for row in data:
        spamwriter.writerow({'mass': row[0], 'length': row[1]})

