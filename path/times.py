#!/usr/bin/env python3
import sys
import os
import argparse
from pathlib import Path
from datetime import datetime
import subprocess

# atime = last time file was accessed
# ctime = last time metadata changed
# mtime = last time contents were modified

def compress_maybe(dir, age):
    print(f'Performing actions on directory {dir}')

    today = datetime.now()

    glob_list = list(dir.glob('*[!.xz]'))
    file_list = [f for f in glob_list if f.is_file()]
    print(file_list)
    if file_list:
        for f in file_list:
            print(f'{f} is a file')
            atime = datetime.fromtimestamp(os.path.getatime(f))
            ctime = datetime.fromtimestamp(os.path.getctime(f))
            mtime = datetime.fromtimestamp(os.path.getmtime(f))
            da = today - atime
            dc = today - ctime
            dm = today - mtime
            print(f'  atime = {atime}; delta = {da}')
            print(f'  ctime = {ctime}; delta = {dc}')
            print(f'  mtime = {mtime}; delta = {dm}')

            print(f'  atime older than {age} days? {da.days > age}')
            print(f'  ctime older than {age} days? {dc.days > age}')
            print(f'  mtime older than {age} days? {dm.days > age}')

            if dc.days > age:
                print(f'ctime > {age} -- compressing {f} ...')
                subprocess.run(['xz', f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            print()
    else:
        print('No uncompressed log files')

def main():
    parser = argparse.ArgumentParser(description='Foo Bar.')
    parser.add_argument('-d', '--debug', action='store_true', help='debug')
    parser.add_argument('-a', '--age', type=int, default=60, help='threshold age for compression in days')
    parser.add_argument('-e', '--expiration', type=int, default=180, help='threshold age for deletion in days')
    parser.add_argument('directory', metavar='DIR', help='directory')
    args = parser.parse_args()

    print(f'args = {args}')

    dir = Path(args.directory)
    if dir.is_dir():
        print(f'{dir} is a directory')
        compress_maybe(dir, args.age)
    else:
        print(f'ERROR: {dir} is not a directory')
        sys.exit(1)


if __name__ == '__main__':
    main()
