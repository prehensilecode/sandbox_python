#!/usr/bin/env python3
import sys, os
import csv
from itertools import cycle, islice
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.ticker as mtick
from matplotlib.colors import Normalize
import numpy as np
from numpy.random import rand
import argparse

mpl.style.use('ggplot')

def testing():
    # https://stackoverflow.com/questions/18903750/vary-the-color-of-each-bar-in-bargraph-using-particular-value
    print('testing()')
    fig, ax = plt.subplots(1, 1)

    # some boring fake data
    my_data = 5*rand(5)
    ax.bar(range(5), rand(5), color=[[0,0,0,1],[0,0,0,1],[1,0.7,0,1],[0,0,0,1],[0,0,0,1]])

    #plt.show()

    plt.savefig('bars.svg', format='svg')


def testing2():
    print('testing2()')
    d = {'one' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
         'two' : pd.Series([11., 12., 13., 14.], index=['a', 'b', 'c', 'd'])}

    df = pd.DataFrame(d)
    print(df)
    subdf = df[['one']]
    print(subdf)

    #mycolors = ['grey', 'red', 'grey', 'grey']
    ### The tuple in list is a workaround due to a bug https://github.com/pandas-dev/pandas/issues/16822
    mycolors = [('grey', 'red', 'grey', 'grey')]

    ax = subdf.plot(kind='bar', color=mycolors)

    plt.xticks(rotation=0)
    plt.tight_layout()

    fig = ax.get_figure()
    fig.savefig('testing2.svg')


def testing3(charges_df):
    fig, ax = plt.subplots()

    print('charges_df')
    print(charges_df)
    print('')
    print('charges_df.index')
    print(charges_df.index)
    print('')
    print('charges_df.values')
    print(charges_df.values)
    print('')

    ax.bar(charges_df.index, charges_df.values, width=0.72)
    plt.title('USING PLT DIRECTLY')
    plt.tight_layout()
    fig.savefig('foo_plt.svg')


def make_all_plots(reportcsv):
    print(type(reportcsv))
    charges_df = pd.read_csv(reportcsv)

    print(charges_df.describe())
    print('')
    print(charges_df.head(5))

    mask = (charges_df['CPU charge ($)'] > 0)

    cpu_charges_df = charges_df[mask][['Last name', 'CPU charge ($)']].sort_values(by=['CPU charge ($)'], ascending=False)

    mycolors = []
    pis = []
    for i,r in cpu_charges_df.iterrows():
        pis.append(r[0])

    for pi in pis:
        for i,r in cpu_charges_df.iterrows():
            #print('i= {} ;  r[0] = {}'.format(i, r[0]))
            if r[0] == pi:
                #mycolors.append('red')
                mycolors.append([1,0.2,0.2,1])
            else:
                #mycolors.append('cyan')
                mycolors.append([0.8,0.8,0.9,1])

        ### XXX
        #mycolors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(cpu_charges_df)))

        #print(mycolors)

        ax = cpu_charges_df.plot(kind='bar', color=[mycolors], width=0.8)

        #ax.set_xticklabels(cpu_charges_df['Last name'])
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False) # labels along the bottom edge are off
        ax.legend_.remove()

        fmt = '$%.0f'
        #fmt = '$%:,.0f'
        #fmt = '${x:,.0f}'
        tick = mtick.FormatStrFormatter(fmt)
        ax.yaxis.set_major_formatter(tick)

        plt.ylabel('CPU charge')

        plt.xlabel('PI')
        #plt.xticks(rotation=45)
        plt.tight_layout()

        fig = ax.get_figure()
        fig.savefig('plot_{}.svg'.format(pi))

        # reset
        mycolors = []

    return charges_df


def make_one_plot():
    pass


def main():
    parser = argparse.ArgumentParser(description='Make barchart from csv.')
    parser.add_argument('-d', '--debug', help='Debugging output', action='store_true')
    parser.add_argument('reportcsv', type=argparse.FileType('r'), help='Summary usage csv file')
    args = parser.parse_args()

    print(type(args.reportcsv))
    print(args.reportcsv.__dict__)
    make_all_plots(args.reportcsv)

    

if __name__ == '__main__':
    #testing()
    #testing2()
    charges_df = main()
    #testing3(charges_df)

