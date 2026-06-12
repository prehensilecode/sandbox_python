#!/usr/bin/env python3
import sys
import os
import delorean


def main():
    print("foo")
    print(f'{os.getenv("HOME")}')


if __name__ == '__main__':
    main()

