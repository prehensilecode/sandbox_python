#!/usr/bin/env python3.10
# Source: https://stackoverflow.com/a/56181933/299952

import numpy as np
import matplotlib.pyplot as plt


ones = np.ones(4)
xfeature = np.asarray([0,1,2,3])
squaredfeature = xfeature ** 2
b = np.asarray([1,2,0,3])

print(f'len(ones) = {len(ones)}')
print(f'len(xfeature) = {len(xfeature)}')
print(f'len(squaredfeature) = {len(squaredfeature)}')
print(f'len(b) = {len(b)}')

features = np.concatenate((np.vstack(ones),np.vstack(xfeature),np.vstack(squaredfeature)), axis = 1) # Change - remove the y values

determinants = np.linalg.lstsq(features, b, rcond=None)[0] # Change - use least squares
plt.scatter(xfeature,b)
u = np.linspace(0,3,100)
plt.plot(u, u**2*determinants[2] + u*determinants[1] + determinants[0] )
plt.show()
