#!/usr/bin/env python3
import sys
import os
import ldap3

server = ldap3.Server('picottemgmt.cm.cluster', port=636, use_ssl=True, get_info=ldap3.ALL)

try:
    username = "cn=Manager, o=cm.cluster"
    password  = "secret"

    conn = ldap3.Connection(server, username, password, auto_bind=True)
    print('Server info: ', server.info)
    #print('Server schema: ', server.schema)
    
    # Any errors will throw an ldap.LDAPError exception 
    # or related exception so you can ignore the result

    ## The next lines will also need to be changed to support your search requirements and directory
    #baseDN = "cn=root,dc=cm,dc=cluster"
    baseDN = "ou=Group,dc=cm,dc=cluster"
    searchScope = ldap3.SUBTREE
    ## retrieve all attributes - again adjust to your needs - see documentation for more options
    retrieveAttributes = None 
    #searchFilter = "cn=*"
    #searchFilter = "cn=d*,objectClass=posixAccount"
    #searchFilter = "uid=*"
    #searchFilter = "uid=*"
    #searchFilter = "objectClass=posixAccount"
    #searchFilter = "(objectClass=posixGroup)"
    searchFilter = "(cn=*)"


    #status, result, response, _ = conn.search('uid=dwc62', '(objectclass=*)')
    #print(status, result, response)

    retval = conn.search(baseDN, searchFilter)
    entries = conn.entries

    print(entries)

except Exception as e:
    print(e)
    # handle error however you like

