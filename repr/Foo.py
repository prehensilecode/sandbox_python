#!/usr/bin/env python3
import sys
import os

class Foo:
    def __init__(self):
        self.data = 'foo'
        self.aloha = 'bar'

    def __repr__(self):
        reprstr = 'Data: {}'.format(self.data)
        reprstr = '\n'.join((reprstr, 'Aloha: {}'.format(self.aloha)))
        return reprstr


if __name__ == '__main__':
    f = Foo()
    print(f)

