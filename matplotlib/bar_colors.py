#!/usr/bin/env python3
import sys, os
import csv
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from numpy.random import rand
import argparse

# https://stackoverflow.com/questions/18903750/vary-the-color-of-each-bar-in-bargraph-using-particular-value

def main():
    parser = argparse.ArgumentParser(description='Make barchart from csv.')
    parser.add_argument('-d', '--debug', help='Debugging output', action='store_true')
    parser.add_argument('reportcsv', type=argparse.FileType('r'), help='Summary usage csv file')
    args = parser.parse_args()

    print('hello')


if __name__ == '__main__':
    fig, ax = plt.subplots(1, 1)
    # get a color map
    my_cmap = cm.get_cmap('jet')
    # get normalize function (takes data in range [vmin, vmax] -> [0, 1])
    my_norm = Normalize(vmin=0, vmax=5)
    # some boring fake data
    my_data = 5*rand(5)
    print(my_cmap(my_norm(my_data)))
    #ax.bar(range(5), rand(5), color=my_cmap(my_norm(my_data)))
    ax.bar(range(5), rand(5), color=[[0,0,0,1],[0,0,0,1],[1,0.7,0,1],[0,0,0,1],[0,0,0,1]])

    plt.show()

    main()

