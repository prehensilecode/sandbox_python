#!/usr/bin/env python3
import sys
import os
import requests
import json
from getpass import getpass

query = {'lat': '45', 'lon': '180'}
#response = requests.get("http://api.open-notify.org/astros.json", params=query)
url = 'https://log-dev.concept2.com/'
headers = {'Accept': 'application/vnd.c2logbook.v1+json'}
response = requests.get(url, headers=headers)
print("JSON:")
print(response.json())
for k, v in response.json().items():
    print(k, v)

print('')
print('dumps')

json.dumps(response.json())

<<<<<<< HEAD
print('headers:')
print(response.headers)

print('status code:')
print(response.status_code)
=======
print('')
>>>>>>> b93c55338dac598dee7e19dd54ab68039c4389ff
