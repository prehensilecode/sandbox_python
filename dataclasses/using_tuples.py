#!/usr/bin/env python3
import sys
import os
from dataclasses import dataclass, field
from typing import Tuple

@dataclass(frozen=True)
class Project:
    name: str
    costcenter: Tuple[int] = field(default_factory=tuple)

    def __hash__(self):
        return hash(self.name)


p = Project(name='foobar', costcenter=(123456, 7890))
print(p)
