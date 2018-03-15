#!/usr/bin/env python3
import sys
import os

class Foobar:
    def __init__(self, aloha='ALOHA', foobar='FOOBAR'):
        self.aloha = aloha
        self.foobar = foobar

    def do_something(self):
        for v in ['aloha', 'foobar']:
            print(self.__dict__[v])


if __name__ == '__main__':
    f = Foobar()
    f.do_something()

    g = Foobar('WHATSUP', 'GOODBYE')
    g.do_something()

