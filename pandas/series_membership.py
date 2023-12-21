#!/usr/bin/env python
import pandas as pd

name_list = ['Abe', 'Bea', 'Cee', 'Dee']

name_ser = pd.Series(name_list)

print('Abe' in name_ser.array)
print('John' in name_ser.array)
