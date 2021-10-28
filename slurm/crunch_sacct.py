#!/usr/bin/env python3
import sys
import os
import csv
import re
import pandas as pd
from datetime import datetime, timedelta
from delorean import Delorean, parse

debug_p = False

batch_pat = re.compile(r'\d+\.batch$')
extern_pat = re.compile(r'\d+\.extern$')

csv.register_dialect('sacct', delimiter='|')

job_data = []
with open('sacct_output.txt', 'r') as sacct_output:
    reader = csv.DictReader(sacct_output, dialect='sacct')

    for row in reader:
        if batch_pat.search(row['JobID']) or extern_pat.search(row['JobID']):
            # print("Found 'batch' or 'extern'")
            pass
        else:
            submit_time = parse(row['Submit'])
            start_time = parse(row['Start'])
            wait_time = start_time - submit_time
            el_h, el_m, el_s = (x for x in row['Elapsed'].split(':'))

            el_d = 0
            if len(el_h.split('-')) == 2:
                el_d, el_h = (int(x) for x in el_h.split('-'))
            else:
                el_h = int(el_h)

            el_m = int(el_m)
            el_s = int(el_s)

            elapsed_time = timedelta(days=el_d, hours=el_h, minutes=el_m, seconds=el_m)

            if debug_p:
                print(f'submit_time = {submit_time}')
                print(f'start_time = {start_time}')
                print(f'wait_time = {wait_time}')
                print(f'elapsed time = {el_d} days {el_h} hrs {el_m} min {el_s} sec')

            job_data.append({'Submit': submit_time, 'Start': start_time, 'Wait': wait_time, 'Wallclock': elapsed_time})

job_df = pd.DataFrame(job_data)

print(job_df.describe())
