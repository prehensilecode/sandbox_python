#!/usr/bin/env python3
import pandas as pd

df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
print('df = ')
print(df)

print()
print('df.pivot(index="foo", columns="bar", values="baz")')
print(df.pivot(index='foo', columns='bar', values='baz'))

