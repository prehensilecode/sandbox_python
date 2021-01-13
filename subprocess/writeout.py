#!/usr/bin/env python3
import sys, os, subprocess
import shutil

### wrong
#subprocess.run(['ls', '-l', '>', 'foobar.txt'])

### right?
with open('foobar.txt', 'w') as f:
    subprocess.run(['sinfo', '--Node', '-o', '%12N %.6D %4P %.11T %.4c %.8z %.8m %.8d %.6w %.8f %58E'], stdout=f)

