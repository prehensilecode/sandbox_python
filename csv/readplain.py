#!/usr/bin/env python3
import csv
import delorean

with open('plain.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(f'{row[0]}    {delorean.parse(row[1])}')

