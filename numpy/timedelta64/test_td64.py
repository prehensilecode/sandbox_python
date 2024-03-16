#!/usr/bin/env python3
import numpy as np

dt = np.timedelta64(360, 's')
print(f'dt = {dt}')

print(f'np.iinfo(np.timedelta64) = {np.iinfo(np.timedelta64)}')
