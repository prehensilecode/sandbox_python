#!/usr/bin/env python3
import sys
import os
import base64

foo = str(base64.b32encode("F938EAF6295A55249B2EC300EDE33F98976C050C".encode("utf-8")))
print(f'{foo}')
