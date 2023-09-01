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

verbose_p = False

def compress_maybe(dir, age):
    global verbose_p

    now = datetime.now()

    glob_list = list(dir.glob('*[!.xz]'))
    file_list = [f for f in glob_list if f.is_file()]
    if file_list:
        for f in file_list:
            atime = datetime.fromtimestamp(os.path.getatime(f))
            mtime = datetime.fromtimestamp(os.path.getmtime(f))
            dm = now - mtime

            if dm.days > age:
                if verbose_p:
                    print(f'ctime > {age} days -- compressing {f} ...')

                try:
                    subprocess.check_call(['/bin/xz', f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    # modify atime and mtime if root
                    if os.geteuid() == 0:
                        fxz = Path(str(f) + '.xz')
                        os.utime(fxz, times=[atime, mtime])
                except CalledProcessError as error:
                    print(f'ERROR: {error.cmd} - {error.stderr}')
                    sys.exit(error.returncode)
    else:
        if verbose_p:
            print('no uncompressed log files')


def delete_maybe(dir, expiration):
    global verbose_p

    now = datetime.now()

    file_list = [f for f in dir.glob('*') if f.is_file()]
    if file_list:
        for f in file_list:
            mtime = datetime.fromtimestamp(os.path.getmtime(f))
            dm = now - mtime

            if dm.days > expiration:
                if verbose_p:
                    print(f'ctime > {age} days -- compressing {f} ...')

                try:
                    subprocess.check_call(['/bin/rm', '-f', f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except CalledProcessError as error:
                    print(f'ERROR: {error.cmd} - {error.stderr}')
                    sys.exit(error.returncode)

def main():
    parser = argparse.ArgumentParser(description='Simple logfile rotation')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose')
    parser.add_argument('-a', '--age', type=int, default=60, help='threshold age for compression in days')
    parser.add_argument('-e', '--expiration', type=int, default=180, help='threshold age for deletion in days')
    parser.add_argument('directory', metavar='DIR', help='directory')
    args = parser.parse_args()

    dir = Path(args.directory)
    if dir.is_dir():
        compress_maybe(dir, args.age)
        delete_maybe(dir, args.expiration)
    else:
        print(f'ERROR: {dir} is not a directory')
        sys.exit(1)


if __name__ == '__main__':
    main()

