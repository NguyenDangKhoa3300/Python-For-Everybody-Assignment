# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 23:17:23 2023

@author: mrpot
"""

import urllib.request, urllib.parse, urllib.error
import json

lst = list()
counts = 0
url = input("Enter a url: ")
handle = urllib.request.urlopen(url).read()

# convert json to python
info = json.loads(handle)

#print(type(info))
#print(len(info))

lst = info['comments']

for item in lst:
    counts += item['count']

print(counts)