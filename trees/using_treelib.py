#!/usr/bin/env python3
import sys
import os
from treelib import Node, Tree

tree = Tree()
tree.create_node('CEO', 'CEO')  # root
tree.create_node('VP_1', 'VP_1', parent='CEO')
tree.create_node('VP_2', 'VP_2', parent='CEO')
tree.create_node('GM_1', 'GM_1', parent='VP_1')
tree.create_node('GM_2', 'GM_2', parent='VP_2')
tree.show()
