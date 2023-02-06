#!/usr/bin/env python3

# https://stackoverflow.com/questions/4628290/pairs-from-single-list

def pairwise(t):
    it = iter(t)
    return zip(it, it)

def chunkwise(t, size=2):
    it = iter(t)
    return zip(*[it]*size)

foo = [1, 2, 3, 4, 5, 6]

print(list(pairwise(foo)))
print(list(chunkwise(foo)))
print(list(chunkwise(foo, 3)))

