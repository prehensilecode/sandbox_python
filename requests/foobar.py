#!/usr/bin/env python3
import sys
import os
import requests
import json

query = {'lat': '45', 'lon': '180'}
response = requests.get("http://api.open-notify.org/astros.json", params=query)
print("JSON:")
print(response.json())
for k, v in response.json().items():
    print(k, v)

print('')
print('dumps')

json.dumps(response.json())

print('')
