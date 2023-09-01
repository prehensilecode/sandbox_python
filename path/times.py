#!/usr/bin/env python3

import os
import argparse
from pathlib import Path
from datetime import datetime
import subprocess


def do_it(dir):
    print(f'Performing actions on directory {dir}')

    file_list = list(dir.glob('*.log'))
    if file_list:
        for f in file_list:
            if f.is_file():
                print(f'{f} is a file')
                print(f'  atime = {datetime.fromtimestamp(os.path.getatime(f))}')
                print(f'  ctime = {datetime.fromtimestamp(os.path.getctime(f))}')
                print(f'  mtime = {datetime.fromtimestamp(os.path.getmtime(f))}')
                print()

            subprocess.run(['xz', f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        print('No .log files')

def main():
    parser = argparse.ArgumentParser(description='Foo Bar.')
    parser.add_argument('-d', '--debug', action='store_true', help='debug')
    parser.add_argument('directory', metavar='DIR', help='directory')
    args = parser.parse_args()

    dir = Path(args.directory)
    if dir.is_dir():
        print(f'{dir} is a directory')
        do_it(dir)
    else:
        print(f'{dir} is not a directory')


if __name__ == '__main__':
    main()
