#!/usr/bin/env python3.6
import sys
import os
import sqlite3


# student: student_id, first_name, last_name
# classes: class_id, name, teacher_id
# student_classes: class_id, student_id     # the junction table


with sqlite3.connect('m2m.db') as conn:
    c = conn.cursor()

    # create tables
    c.execute('''CREATE TABLE students
                (student_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)''')

    
    c.execute('''CREATE TABLE classes
                (class_id INTEGER PRIMARY KEY, name TEXT, teacher_id INTEGER)''')

    c.execute('''CREATE TABLE students_classes
                (class_id INTEGER, student_id INTEGER)''')


    # populate tables
    students = [(1, 'John', 'Lee'),
                (2, 'Jane', 'Wilson'),
                (3, 'Daniel', 'Gomez')]
    c.executemany('INSERT INTO students VALUES (?,?,?)', students)

    classes = [(1, 'Biology', 2),
               (2, 'Physics', 4),
               (3, 'English', 77)]
    c.executemany('INSERT INTO classes VALUES (?,?,?)', classes)

    students_classes = [(1, 2), 
                        (1, 3),
                        (2, 2),
                        (3, 1)]
    c.executemany('INSERT INTO students_classes VALUES (?,?)', students_classes)


    # all students taking bio
    print("All students taking Bio")
    for row in c.execute('''SELECT s.student_id, last_name
          FROM students_classes sc 
          INNER JOIN students s ON s.student_id = sc.student_id
          WHERE sc.class_id = 1'''):
        print(row)
    print("")


    # all classes taken by Jane Wilson
    print("All classes taken by Jane Wilson")
    for row in c.execute('''SELECT c.class_id, name
          FROM students_classes sc 
          INNER JOIN classes c ON c.class_id = sc.class_id
          WHERE sc.student_id = 2'''):
        print(row)
    print("")

conn.close()
