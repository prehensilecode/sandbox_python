#!/usr/bin/env python3
# From: https://stackoverflow.com/a/57812852/299952
DEBUG = True


def debug_print_maybe(fstr):
    global DEBUG

    if DEBUG:
        print(eval(f'f"DEBUG: {fstr}"'))


a = 13
b = 'foobar'

print(f'DEBUG = {DEBUG}')
debug_print_maybe('a = {a}; b = {b}')

DEBUG = False
print(f'DEBUG = {DEBUG}; expect nothing after this')
debug_print_maybe('a = {a}; b = {b}')

