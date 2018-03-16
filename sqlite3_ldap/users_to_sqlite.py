#!/usr/bin/env python3.6
import sys
import os
import ldap
import sqlite3

#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

# insert row
#c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

# commit changes
#conn.commit()

#conn.close()


try:
    l = ldap.open('127.0.0.1')
    l.protocol_version = ldap.VERSION3
    username = 'cn=rogroup,dc=cm,dc=cluster'
    password = ''
    l.simple_bind(username, password)

    conn = sqlite3.connect('proteususers.db')
    c = conn.cursor()
    #c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
    #c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")
    conn.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS proteususers (
        distinguished_name TEXT PRIMARY KEY,
        uid                TEXT NOT NULL,
        common_name        TEXT NOT NULL,
        surname            TEXT NOT NULL,
        mail               TEXT
        )''')
    conn.commit()



    ## The next lines will also need to be changed to support your search requirements and directory
    #baseDN = "cn=root,dc=cm,dc=cluster"
    baseDN = "dc=cm,dc=cluster"
    searchScope = ldap.SCOPE_SUBTREE
    ## retrieve all attributes - again adjust to your needs - see documentation for more options
    retrieveAttributes = None 
    searchFilter = "cn=*"
    #searchFilter = "cn=d*,objectClass=posixAccount"
    #searchFilter = "uid=*"
    searchFilter = "objectClass=posixAccount"
    #searchFilter = "objectClass=posixGroup"

    try:
        ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_set = []
        while 1:
            result_type, result_data = l.result(ldap_result_id, 0)
            if (result_data == []):
                break
            else:
                ## here you don't have to append to a list
                ## you could do whatever you want with the individual entry
                ## The appending to list is just for illustration. 
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)


        irregular_users = ['cmsupport', 'HPL', 'dwchin', ]

        res_tuples = []
        for x in result_set:
            #print(x)
            #print(x[0])
            #for k,v in x[0][1].items():
            #    print(k, v)
            #print(" ")

            dn  = x[0][0]
            uid = x[0][1]['uid'][0].decode('utf-8')

            if uid not in irregular_users:
                cn  = x[0][1]['cn'][0].decode('utf-8')
                sn  = x[0][1]['sn'][0].decode('utf-8')
                mail = x[0][1]['mail'][0].decode('utf-8')

                res_tuples.append((dn, uid, cn, sn, mail))

            
        #print(type(result_set[0][0]))
        #print(result_set[0][0][0])
        #for k, v in result_set[0][0][1].items():
        #    print(k, v)

        c.executemany('INSERT INTO proteususers VALUES (?, ?, ?, ?, ?)', res_tuples)

    except ldap.LDAPError as lerr:
        print(lerr)


    for row in c.execute('SELECT * FROM proteususers ORDER BY surname'):
        print(row)

    print('')

    print('Search for "Halley"')
    t = ('Halley',)
    c.execute('SELECT * FROM proteususers WHERE surname=?', t)
    print(c.fetchone())

except (ldap.LDAPError, sqlite3.Error) as e:
    print(e)

conn.close()

sys.exit(0)

