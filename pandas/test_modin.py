#!/usr/bin/env python3.9
import sys
import os
import time
import numpy as np
import pandas as pd


frame_data = np.random.randint(0, 100, size=(2 ** 10, 2 ** 8))

tic = time.perf_counter()
df = pd.DataFrame(frame_data)
toc = time.perf_counter()

print(f"{toc - tic:0.4e} seconds")


tic = time.perf_counter()
df2 = pd.read_csv("data.csv")
toc = time.perf_counter()
print(f"Read big CSV file: {toc - tic:0.4e} seconds")
