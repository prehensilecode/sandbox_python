#!/usr/bin/env python3.6
import sys
import os
import ldap

try:
    l = ldap.open("127.0.0.1")
    
    # you should  set this to ldap.VERSION2 if you're using a v2 directory
    l.protocol_version = ldap.VERSION3  
    # Pass in a valid username and password to get 
    # privileged directory access.
    # If you leave them as empty strings or pass an invalid value
    # you will still bind to the server but with limited privileges.
    
    #username = "cn=Manager, o=cm.cluster"
    username = "cn=rogroup,dc=cm,dc=cluster"
    #password  = "secret"
    password  = ""
    
    # Any errors will throw an ldap.LDAPError exception 
    # or related exception so you can ignore the result
    l.simple_bind(username, password)
except ldap.LDAPError as e:
    print(e)
    # handle error however you like


## The next lines will also need to be changed to support your search requirements and directory
#baseDN = "cn=root,dc=cm,dc=cluster"
baseDN = "dc=cm,dc=cluster"
searchScope = ldap.SCOPE_SUBTREE
## retrieve all attributes - again adjust to your needs - see documentation for more options
retrieveAttributes = None 
searchFilter = "cn=*"
#searchFilter = "cn=d*,objectClass=posixAccount"
#searchFilter = "uid=*"
#searchFilter = "objectClass=posixAccount"
searchFilter = "objectClass=posixGroup"

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

    for x in result_set:
        #print(x)
        print(x[0][0])
        for k,v in x[0][1].items():
            print(k, v)
        print(" ")

    #print(type(result_set[0][0]))
    #print(result_set[0][0][0])
    #for k, v in result_set[0][0][1].items():
    #    print(k, v)

except ldap.LDAPError as e:
    print(e)
