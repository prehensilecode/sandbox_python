#!/usr/bin/env python3.6
import sys
import os
import sqlite3

# from https://stackoverflow.com/questions/6935620/sqlite-many-to-many-relationship

with sqlite3.connect('foobar.db') as conn:
    c = conn.cursor()
    c.execute('''CREATE TABLE foo(
        id INTEGER PRIMARY KEY NOT NULL,
        foo_col INTEGER NOT NULL
        );''')
    c.execute('''CREATE TABLE bar(
        id INTEGER PRIMARY KEY NOT NULL,
        bar_col INTEGER NOT NULL
        );''')
    c.execute('''CREATE TABLE foobar(
            foo_id INTEGER,
            bar_id INTEGER,
            FOREIGN KEY(foo_id) REFERENCES foo(id) ON DELETE CASCADE,
            FOREIGN KEY(bar_id) REFERENCES bar(id) ON DELETE CASCADE
        );''')
    c.execute('''CREATE INDEX fooindex ON foobar(foo_id);''')
    c.execute('''CREATE INDEX barindex ON foobar(bar_id);''')
    conn.commit()

    foos = []
    for i in range(6):
        foos.append((None, i+100))
    
    c.executemany('INSERT INTO foo VALUES (?,?)', foos)
    conn.commit()

    print('foos')
    for row in c.execute('SELECT * FROM foo ORDER BY id'):
        print(row)
    print("")

    bars = []
    for i in range(6):
        bars.append((None, i+200))

    c.executemany('INSERT INTO bar VALUES (?,?)', bars)
    conn.commit()

    print('bars')
    for row in c.execute('SELECT * FROM bar ORDER BY id'):
        print(row)
    print("")

    foobars = []
    for i in range(6):
        #print('foobars: i = {}'.format(i))
        foobars.append((i, 5-i))

    c.executemany('INSERT INTO foobar VALUES (?,?)', foobars)
    conn.commit()

    print('foobars')
    for row in c.execute('SELECT * FROM foobar ORDER BY foo_id'):
        print('type(row) = {}, row = {}'.format(type(row), row))

    print("")

conn.close()
os.remove('foobar.db')

