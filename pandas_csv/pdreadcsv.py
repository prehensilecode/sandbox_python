#!/usr/bin/env python3
import sys, os
import csv
import pandas as pd
import argparse


def read_foo_csv(csvfile):
    print('read_csv(): type(csvfile)) = {}'.format(csvfile))
    print('')

    foo_df = pd.read_csv(csvfile)

    return foo_df


def main():
    parser = argparse.ArgumentParser(description='Make barchart from csv.')
    parser.add_argument('-d', '--debug', help='Debugging output', action='store_true')
    parser.add_argument('csvfile', type=argparse.FileType('r'), help='Input csv file')
    args = parser.parse_args()

    print('main(): type(args.csvfile)) = {}'.format(args.csvfile))
    print('')

    ### This works 
    #foo_df = pd.read_csv(args.csvfile)

    #print(foo_df.describe())
    #print('')
    #print(foo_df.head(5))
    #print('')

    ### This does not work if the above is uncommented because the stream has been exhausted
    foo_df = read_foo_csv(args.csvfile)

    print(foo_df.describe())
    print('')
    print(foo_df.head(5))


if __name__ == '__main__':
    main()

