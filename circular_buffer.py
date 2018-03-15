#!/usr/bin/env python3
import sys
import os
from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    print(res)
    deque(map(deque.rotate, res, range(n)), 0)
    return [list(d) for d in res]

foo = doodledPassword([1,2,3])
print(foo)

