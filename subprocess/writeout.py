#!/usr/bin/env python3
import sys, os, subprocess
import shutil

### wrong
#subprocess.run(['ls', '-l', '>', 'foobar.txt'])

### right?
with open('foobar.txt', 'w') as f:
    subprocess.run(['ls', '-l'], stdout=f)

