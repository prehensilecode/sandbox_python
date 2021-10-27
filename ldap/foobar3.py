#!/usr/bin/env python3
import sys
import os
import ldap3
from datetime import datetime, timedelta
from delorean import Delorean, epoch

unix_epoch = epoch(0)

server = ldap3.Server('picottemgmt.cm.cluster', port=636, use_ssl=True, get_info=ldap3.ALL)

try:
    #username = "cn=Manager, o=cm.cluster"
    #password = "secret"
    username = "cn=readonlyroot,dc=cm,dc=cluster"
    password  = "pJUO7SJmir3Qpl9Q"
    #username = "cn=rogroup,dc=cm,dc=cluster"

    conn = ldap3.Connection(server, username, password, auto_bind=True)
    print('Server info: ', server.info)
    # print('Server schema: ', server.schema)
    print('')

    # Any errors will throw an ldap.LDAPError exception 
    # or related exception so you can ignore the result

    ## The next lines will also need to be changed to support your search requirements and directory
    #baseDN = "cn=root,dc=cm,dc=cluster"
    #baseDN = "ou=Group,dc=cm,dc=cluster"
    baseDN = "dc=cm,dc=cluster"
    searchScope = ldap3.SUBTREE
    #searchFilter = "(cn=*)"
    #searchFilter = "(&(uid=*))"
    searchFilter = "(uid=dwc62)"
    #searchFilter = "cn=d*,objectClass=posixAccount"
    #searchFilter = "uid=*"
    #searchFilter = "uid=*"
    #searchFilter = "objectClass=posixAccount"
    #searchFilter = "(objectClass=posixGroup)"
    #searchFilter = "(cn=*)"


    #status, result, response, _ = conn.search('uid=dwc62', '(objectclass=*)')
    #print(status, result, response)

    #retval = conn.search(baseDN, searchFilter)
    #entries = conn.entries
    #conn.search('dc=cm,dc=cluster', '(&(objectclass=person)(uid=dwc62))')
    #conn.search('dc=cm,dc=cluster', '(&(objectclass=posixgroup)(cn=liangGrp))')
    #conn.search('cn=schema', '(objectclass=*)')
    conn.search(search_base=baseDN,
                search_scope=searchScope,
                search_filter=searchFilter,
                attributes=['*']
                )

    if len(conn.entries) > 1:
        print(f'Found {len(conn.entries)} entries.')
    else:
        print(f'Found {len(conn.entries)} entry.')

    for entry in conn.entries:
        print(f'type(entry) = {type(entry)}')
        print(f'entry attributes as dict = {entry.entry_attributes_as_dict}')
        dt = timedelta(days=entry.entry_attributes_as_dict["shadowExpire"][0])
        print(f'Exp. day = {dt}')
        datestamp = unix_epoch + dt
        formatted_date = datestamp.datetime.strftime("%Y-%m-%d")
        formatted_date = datestamp.datetime.strftime("%x")
        formatted_date = datestamp.datetime.strftime("%b %d, %Y")
        print(f'Exp. date = {formatted_date}')

    # XXX shadowExpire=25566 = 2039/12/30

except Exception as e:
    print(e)
    # handle error however you like

