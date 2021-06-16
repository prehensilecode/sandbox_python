#!/usr/bin/env python3
import sys
import os
import numpy as np
import time

debug_p = False

def use_for_loop(mat_a, mat_b):
    # Return mat_a x mat_b 
    print('Doing matrix multiply using for loops')
    m = mat_a.shape[0]
    n = mat_a.shape[1]
    p = mat_b.shape[1]

    if debug_p:
        print(f'm = {m}, n = {n}, p = {p}')

    if mat_b.shape[0] != n:
        print('ERROR: mismatch in dimensions')
        sys.exit(1)

    result = np.zeros([mat_a.shape[0], mat_b.shape[1]])
    for i in range(m):
        for j in range(n):
            for k in range(p):
                result[i, k] += mat_a[i, j] * mat_b[j, k]

    return result


def use_matmul(mat_a, mat_b):
    print('Doing matrix multiply using numpy.matmul')

    return np.matmul(mat_a, mat_b)


def main():
    if debug_p:
        mat_a = np.identity(3)
        mat_b = np.identity(3)
    else:
        mat_a = np.random.rand(500, 500)
        mat_b = np.random.rand(500, 500)

    if debug_p:
        print(f'mat_a = \n{mat_a}')
        print(f'mat_b = \n{mat_b}')

    print(f'mat_a.shape = {mat_a.shape}')
    print(f'mat_b.shape = {mat_b.shape}')
    print('')

    tic = time.time()
    mat_c = use_for_loop(mat_a, mat_b)
    toc = time.time()

    slow = toc - tic

    if debug_p:
        print(f'mat_c = \n{mat_c}')

    print(f'mat_c.shape = {mat_c.shape}')
    print(f'Time taken: {slow:>7.4e} sec.')

    print('')

    tic = time.time()
    mat_d = use_matmul(mat_a, mat_b)
    toc = time.time()
    fast = toc - tic
    print(f'mat_d.shape = {mat_d.shape}')
    print(f'Time taken: {fast:>7.4e} sec.')

    print('')

    print(f'Check that results are same: norm of difference between two results = {np.linalg.norm(mat_c - mat_d):.4e}')

    print('')
    print(f'Speedup = {slow / fast:>.2f} times')




if __name__ == '__main__':
    main()

