#!/usr/bin/env python3
import sys
import os
import grp
import operator

all_groups = grp.getgrall()
interesting_groups = sorted((g for g in all_groups
                             if g.gr_name.endswith('Grp')),
                            key=operator.attrgetter('gr_name'))

name_length = max(len(g.gr_name) for g in interesting_groups) + 1

print(f"{'Name':16s} {'GID':>6s} Members")
for g in interesting_groups:
    print(f"{g.gr_name:16s} {g.gr_gid:>6d} {', '.join(g.gr_mem)}")
