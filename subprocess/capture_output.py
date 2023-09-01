#!/usr/bin/env python3
# source: https://stackoverflow.com/a/56918582/299952
import selectors
import subprocess
import sys

p = subprocess.Popen(
    ["python3", "random_out.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

sel = selectors.DefaultSelector()
sel.register(p.stdout, selectors.EVENT_READ)
sel.register(p.stderr, selectors.EVENT_READ)

while True:
    for key, _ in sel.select():
        data = key.fileobj.read1().decode()
        if not data:
            exit()
        if key.fileobj is p.stdout:
            print(data, end="")
        else:
            print(data, end="", file=sys.stderr)

