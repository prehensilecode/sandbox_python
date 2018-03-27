#!/usr/bin/env python3
import sys
import os

class Foo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def xy(self):
        return '{}.{}'.format(self.x, self.y)


if __name__ == '__main__':
    foo = Foo(6,9)
    print(foo.xy())
