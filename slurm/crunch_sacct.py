#!/usr/bin/env python3
import sys
import os
import csv
import re
import io
import subprocess
import pandas as pd
from datetime import datetime, timedelta
from delorean import Delorean, parse

debug_p = False

batch_pat = re.compile(r'\d+\.batch$')
extern_pat = re.compile(r'\d+\.extern$')

csv.register_dialect('sacct', delimiter='|')


project = 'something'
sacct_cmdline = f'/cm/shared/apps/slurm/current/bin/sacct -P -o JobID%20,Submit,Start,Elapsed -T -S2021-08-01-00:00 -E2021-09-01-00:00 -A {project} -a'.split()
if debug_p:
    print(sacct_cmdline)

try:
    sacct_results = subprocess.run(sacct_cmdline, capture_output=True)

    if debug_p:
        print(f'DEBUG: sacct_results = {sacct_results}')

    if sacct_results.returncode == 0:
        sacct_output = sacct_results.stdout
    else:
        print(f'WARNING: sacct return code = {sacct_results.returncode}')
        print(f'    {sacct_results.stder}')
except Exception as e:
    print(f'EXCEPTION: {e}')
    sys.exit(2)


job_data = []
reader = csv.DictReader(io.StringIO(sacct_output.decode('utf-8')), dialect='sacct')

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
