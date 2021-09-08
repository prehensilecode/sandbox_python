#!/usr/bin/env python3.9
import sys
import os
from pathlib import Path

homedir = os.getenv('HOME')
mastersdir = Path(homedir) / 'Pictures' / 'Masters'
for root, dirs, files in os.walk(mastersdir):
    print('root', root)
    print('dirs', dirs)
    print('files', files)
    print('')
