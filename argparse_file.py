#!/usr/bin/env python3
import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('foofile', type=argparse.FileType('w', encoding='latin-1'))

    args = parser.parse_args()

    args.foofile.write('hello, world\n')


if __name__ == '__main__':
    main()

