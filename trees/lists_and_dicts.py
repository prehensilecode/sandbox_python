#!/usr/bin/env python3
import sys
import os

# From https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd

# Using dict
Families = {'Peter': ['Paul', 'Patty'],
            'Jim': ['Tommy', 'Timmy', 'Tammy'],
            'Carlos': ['Diego']}

# NB use of * operator to unpack Children list
for Parent, Children in Families.items():
    print(f'{Parent} has {len(Children)} kid(s):')
    print(f'    {", and ".join([str(Child) for Child in [*Children]])}')

print()

# Using list and enumerate
Prizes = [['Gold Medal', '$10,000', 'Sports Car', 'Brand Sponsorship'],
          ['Silver Medal', '$5,000', 'Budget Car'],
          ['Bronze Medal', '$2,500', 'Motorcycle'],
          ['Participation Trophy', 'Swag'],
          ['Swag']]

for place, prizelist in enumerate(Prizes):
    print(f"Place #{place+1} gets the following prize(s):")
    print(f"    {', and '.join([prize for prize in [*prizelist]])}")

print()

# foo
Families = [['Peter', 'Paul', 'Patty'],
            ['Jim', 'Tommy', 'Timmy', 'Tammy'],
            ['Carlos', 'Diego']]

for Parent, Children in enumerate(Families):
    print(f'{Families[0][0]} has children:')
    print(f'    {", and ".join([str(Child) for Child in [*Children]])}')

print()

# dicts - forest of 3 trees
Families = {
    'Peter': {
        'Paul': {'Dog', 'Toucan'},
        'Patty': {'Turtle'}
    },
    'Jim': {
        'Tommy': {'Hamster'},
        'Timmy': {'Hamster'},
        'Tammy': {'Hamster'}
    },
    'Carlos': {
        'Diego': {'Cat', 'Ferret', 'Fox'}
    }
}

for Parent, Children in Families.items():
    print(f"{Parent} has {len(Children)} kid(s):")
    print(f"    {', and '.join([Child for Child in [*Children]])}")

    for Child, Pets in Children.items():
        print(f"    {Child} has {len(Pets)} pet(s):")
        print(f"        {', and '.join([Pet for Pet in [*Pets]])}")
    print()


# removing all Hamsters
for Parent, Children in Families.items():
    for Child, Pets in Children.items():
        for Pet in Pets:
            if Pet == 'Hamster':
                Families[Parent][Child] = {}

# direct update
Families['Carlos']['Diego'] = {'Cat', 'Ferret'}

for Parent, Children in Families.items():
    print(f"{Parent} has {len(Children)} kid(s):")
    print(f"    {', and '.join([Child for Child in [*Children]])}")

    for Child, Pets in Children.items():
        print(f"    {Child} has {len(Pets)} pet(s):")
        print(f"        {', and '.join([Pet for Pet in [*Pets]])}")
print()

# del
del Families['Peter']['Paul']

for Parent, Children in Families.items():
    print(f"{Parent} has {len(Children)} kid(s):")
    print(f"    {', and '.join([Child for Child in [*Children]])}")

    for Child, Pets in Children.items():
        print(f"    {Child} has {len(Pets)} pet(s):")
        print(f"        {', and '.join([Pet for Pet in [*Pets]])}")
print()


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
