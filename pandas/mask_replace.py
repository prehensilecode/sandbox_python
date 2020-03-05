#!/usr/bin/env python3
import sys
import os
import delorean
import datetime
import pandas as pd
import numpy as np

start = datetime.datetime(2019, 1, 31)
for stop in delorean.stops(freq=delorean.MONTHLY, start=start, count=12, timezone='UTC'):
    print(stop)

