#!/usr/bin/env python3
import sys
import os
import ldap3
from datetime import datetime, timedelta
from delorean import Delorean, epoch

debug_p = True

unix_epoch = epoch(0)

server = ldap3.Server('picottemgmt.cm.cluster', port=636, use_ssl=True, get_info=ldap3.ALL)
username = "cn=readonlyroot,dc=cm,dc=cluster"
password  = input("Read-only password: ")

if debug_p:
    print(f'DEBUG: password = {password}')

users_info = []

gr_mem = ['dca54', 'cl3293', 'el662', 'mm4862',
          'ma3533', 'ec988', 'as4874', 'sc3623', 'zdarynova',
          'bb826', 'ips24', 'egao', 'cw842', 'sr957', 'soa52',
          'dag332', 'yl497', 'tgc37', 'haasj74', 'ecs89', 'sw424',
          'yp93', 'gcd34', 'mag535', 'shsu2', 'jb3455', 'jc3673',
          'ac3499', 'xc349', 'calvin', 'wi24', 'khanj6', 'acn46',
          'nclark16', 'wc492', 'gailr', 'zz374', 'err29', 'jim43',
          'bas44']

try:
    conn = ldap3.Connection(server, username, password, auto_bind=True)
    base_dn = "dc=cm,dc=cluster"
    search_scope = ldap3.SUBTREE

    for u in gr_mem:
        search_filter = f"(uid={u})"
        conn.search(search_base=base_dn,
                    search_scope=search_scope,
                    search_filter=search_filter,
                    attributes=['*']
                    )
        if debug_p:
            print(f'DEBUG: make_user_list(): found {len(conn.entries)} entries.')

        entry_dict = conn.entries[0].entry_attributes_as_dict

        if debug_p:
            print(f'DEBUG: entry_dict = {entry_dict}')

        dt = timedelta(days=entry_dict['shadowExpire'][0])
        exp_datestamp = unix_epoch + dt
        exp_date = exp_datestamp.datetime.strftime('%b %d, %Y')
        users_info.append({'SN': entry_dict['sn'][0], 'CN': entry_dict['cn'][0],
            'Expiration date': exp_date, 'Inactive?': bool(int(entry_dict['shadowInactive'][0])),
            'Email': entry_dict['mail'][0], 'Login shell': entry_dict['loginShell'][0]})
except Exception as e:
    print(f'EXCEPTION: ldap error {e}')
    sys.exit(1)

for u in users_info:
    print(u)

