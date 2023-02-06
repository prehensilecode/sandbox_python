#!/usr/bin/env python3
import sys
import os

# From https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd

# Minimal Tree & Node classes
class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []
        self.nodes = []

    def addNode(self, obj):
        self.children.append(obj)

    def getAllNodes(self):
        self.nodes.append(self.root)
        for child in self.children:
            self.nodes.append(child.data)

        for child in self.children:
            if child.getChildNodes(self.nodes) != None:
                child.getChiuldNodes(self.nodes)
        print(*self.nodes, sep='\n')
        print(f'Tree size: {len(self.nodes)}')

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)

    def getChildNodes(self, Tree):
        for child in self.children:
            if child.children:
                child.getChildNodes(Tree)
            Tree.append(child.data)


FunCorp = Tree('Head Honcho')
print(FunCorp.root)

FunCorp.addNode(Node('VP of Stuff'))
FunCorp.addNode(Node('VP of Shenanigans'))
FunCorp.addNode(Node('VP of Foobar'))

print(f'C suite: {", ".join(child.data for child in FunCorp.children)}')
print()

FunCorp.children[0].addNode(Node('GM of Fun'))
FunCorp.children[1].addNode(Node('GM of Shindigs'))
FunCorp.children[0].children[0].addNode(Node('Sub-manager of Fun'))
FunCorp.children[0].children[0].children[0].addNode(Node('Employee of the month'))

print(f'The position under {FunCorp.children[0].data} is {FunCorp.children[0].children[0].data}')
print()

# get all nodes (unordered)
FunCorp.getAllNodes()

