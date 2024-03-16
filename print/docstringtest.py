#!/usr/bin/env python3
"""
This is the __doc__ string
"""

import sys
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                prog="docstringtest",
                description=__doc__,
                epilog="Footer text")
    args = parser.parse_args()
    print(f'__doc__ == {__doc__}')
