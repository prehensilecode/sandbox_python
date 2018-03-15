#!/usr/bin/env python3
import sys
import os
import xlsxwriter as xw

# create new Excel file and add a worksheet
workbook = xw.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# widen the first column
worksheet.set_column('A:A', 20)

# add bold format
bold = workbook.add_format({'bold': True})

# write some text
worksheet.write('A1', 'Hello')

# text with formatting
worksheet.write('A2', 'World', bold)

# write numbers with row/col notation
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# insert image
worksheet.insert_image('B5', 'logo.png')

workbook.close()

