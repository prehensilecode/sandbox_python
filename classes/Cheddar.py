#!/usr/bin/env python
import sys
import os
from dataclasses import dataclass, field

@dataclass
class Cheddar:
    unit_cost = 1.50
    weight : float = 0.
    ext_cost : float = weight * unit_cost


if __name__ == '__main__':
    c = Cheddar(4.)
    print(c)
    print(c.unit_cost)
