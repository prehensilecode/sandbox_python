#!/usr/bin/env python3.10
# Source: https://stackoverflow.com/a/56181933/299952

import numpy as np
import matplotlib.pyplot as plt


ones = np.ones(4)
xfeature = np.asarray([0,1,2,3])
squaredfeature = xfeature ** 2
b = np.asarray([1,2,0,3])

print(f'ones.shape = {ones.shape}')
print(f'xfeature.shape = {xfeature.shape}')
print(f'squaredfeature.shape = {squaredfeature.shape}')
print(f'b.shape = {b.shape}')

features = np.concatenate((np.vstack(ones),np.vstack(xfeature),np.vstack(squaredfeature)), axis=1) # Change - remove the y values
print(f'features.shape = {features.shape}')


determinants = np.linalg.lstsq(features, b, rcond=None)[0] # Change - use least squares
plt.scatter(xfeature,b)
u = np.linspace(0,3,100)
plt.plot(u, u**2*determinants[2] + u*determinants[1] + determinants[0] )
plt.show()
