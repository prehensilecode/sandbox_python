#!/usr/bin/env python3
import sys
import os

# From https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd

# Minimal Tree & Node classes
class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)


class Node():
    def __init__(self, data):
        self.data = data
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)

FunCorp = Tree('Head Honcho')
print(FunCorp.root)

FunCorp.addNode(Node('VP of Stuff'))
FunCorp.addNode(Node('VP of Shenanigans'))
FunCorp.addNode(Node('VP of Foobar'))

print(f'C suite: {", ".join(child.data for child in FunCorp.children)}')

FunCorp.children[0].addNode(Node('GM of Fun'))

print(f'The position under {FunCorp.children[0].data} is {FunCorp.children[0].children[0].data}')
