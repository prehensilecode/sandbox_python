#!/usr/bin/env python3.9
import numpy as np
import pandas as pd
import fiscalyear as fy

a = fy.FiscalYear(1999)
print(f'Fiscal year a start = {a.start}')
print(f'Fiscal year a end = {a.end}')

b = fy.FiscalYear(2000)
print(f'Fiscal year b start = {b.start}')
print(f'Fiscal year b end = {b.end}')

yearstr = '1999-00' # this is fiscal 2000

myfy = fy.FiscalYear(int(yearstr.split('-')[0]) + 1)
print(myfy.start.fiscal_year)
print(myfy.end.fiscal_year)

test_df = pd.DataFrame(data={
    'Season': ['1996-97', '1997-98', '1998-99', '1999-00', '2000-01',
               '2001-02', '2002-03', '2003-04', '2004-05', '2005-06',
               '2006-07', '2007-08', '2008-09', '2009-10', '2010-11', 
               '2011-12'],
    'Height':np.random.randint(20, size=16),
    'Weight':np.random.randint(40, size=16)
})

print(test_df.describe())

test_df['Season'] = test_df['Season'].apply(lambda x : fy.FiscalYear(int(x[0:4]) + 1).fiscal_year)
print(test_df)
