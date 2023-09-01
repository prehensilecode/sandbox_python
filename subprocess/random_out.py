#!/usr/bin/env python3
# source: https://stackoverflow.com/a/56918582/299952
import sys
from time import sleep

for i in range(10):
    print(f" err{i} ", file=sys.stderr, end="")
    sleep(0.1)
    print(f" out{i} ", end="")
    sleep(0.1)

