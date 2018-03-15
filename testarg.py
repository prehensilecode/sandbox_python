#!/usr/bin/env python3

import sys, os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output-dir', help="output directory", default='.')
args = parser.parse_args()

print(args.output_dir)

outdir = Path(args.output_dir)

if not outdir.exists():
    outdir.mkdir(mode=0o770, parents=True)
elif not outdir.is_dir():
    raise OSError("'%s' is not a directory" % (outdir))

