#!/usr/bin/env python3
import sys
import os
import json
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Person:
   name : str
   species : str


z = Person(name="Zaphod Beeblebrox", species="Betelgeusian")
print(z)

with open('zaphod.json', 'w') as f:
    json.dump(asdict(z), f)
