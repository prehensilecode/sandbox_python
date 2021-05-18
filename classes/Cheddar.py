#!/usr/bin/env python3
import sys
import os
from dataclasses import dataclass, field

@dataclass
class Cheddar:
    unit_cost = 1.50
    weight : float = 0.
    ext_cost : float = weight * unit_cost
    brands : list[str] = field(default_factory=list)


if __name__ == '__main__':
    c = Cheddar(4.)
    c.brands += ['foo', 'bar', 'baz']
    print(c)
    print(c.unit_cost)
