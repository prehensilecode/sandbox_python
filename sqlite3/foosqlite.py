#!/usr/bin/env python3.6
import sys
import os
import sqlite3

conn = sqlite3.connect('foobar.db')

c = conn.cursor()

# create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# insert row
c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

# commit changes
conn.commit()

conn.close()

conn = sqlite3.connect('foobar.db')
c = conn.cursor()
t = ('RHAT', )
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)


conn.commit()
conn.close()

