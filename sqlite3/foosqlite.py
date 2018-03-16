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

