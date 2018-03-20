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
        );
        CREATE TABLE bar(
            id INTEGER PRIMARY KEY NOT NULL,
            bar_col TEXT NOT NULL
        );
        CREATE TABLE foobar(
            foo_id INTEGER,
            bar_id INTEGER,
            FOREIGN KEY(foo_id) REFERENCES foo(id) ON DELETE CASCADE,
            FOREIGN KEY(bar_id) REFERENCES bar(id) ON DELETE CASCADE
        );
        CREATE INDEX fooindex ON foobar(foo_id);
        CREATE INDEX tagindex ON foobar(tag_id);''')
    conn.commit()


