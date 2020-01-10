#!/usr/bin/env python3
import sys
import os
import csv
import argparse
import magic


def reformat_utf16le_maybe(filename):
    suffix = filename.split('.')[1]

    if suffix == 'csv':
        dialect = 'excel'
    elif suffix == 'tsv':
        dialect = 'excel-tab'
    else:
        dialect = 'excel'

    m = magic.Magic(mime=True, mime_encoding=True)
    codec = m.from_file(filename)
    encoding = codec.split(';')[1]

    print('codec = {}'.format(codec))
    print('encoding = {}'.format(encoding))

    return encoding.split('=')[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', help='Debugging')
    parser.add_argument('-s', '--student-csv', required=True, help='CSV or TSV file of student info')
    args = parser.parse_args()

    print(args)

    # file format
    suffix = args.student_csv.split('.')[1]

    print('suffix = {}'.format(suffix))

    if suffix == 'csv':
        dialect = 'excel'
    elif suffix == 'tsv':
        dialect = 'excel-tab'
    else:
        # punt
        dialect = 'excel'

    print('Dialect = {}'.format(dialect))

    encoding = reformat_utf16le_maybe(args.student_csv)
    
    print('returned encoding = {}'.format(encoding))

    with open(args.student_csv, 'r', encoding=encoding) as cf:
        cr = csv.DictReader(cf, dialect=dialect)
        print(cr.fieldnames)
        cr.fieldnames[0] = 'Last Name'
        print(cr.fieldnames)
        
        counter = 0
        for row in cr:
            print(row)
            counter += 1
            #print(row.keys())
            #print(row)


if __name__ == '__main__':
    main()

