#!/usr/bin/env python3
import sys
import os
from datetime import datetime, timedelta
from delorean import Delorean, epoch

now = Delorean()
print(now)

dt = timedelta(days=1)

print(now + dt)

date = datetime(2021, 3, 31, 0, 0, 0)
print(date)
print(date + dt)

shadow_epoch = Delorean(datetime(1970, 1, 1, 0, 0, 0), timezone='UTC')
unix_epoch = epoch(0)
print(f'shadow epoch = {shadow_epoch}')
print(f'unix epoch = {unix_epoch}')
dt = timedelta(days=25566)
print('expected expir. date = 2039/12/30')
print(f'expir. date = {shadow_epoch + dt}')
print(f'expir. date = {unix_epoch + dt}')
