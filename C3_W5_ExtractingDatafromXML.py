# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 00:21:39 2023

@author: mrpot
"""
# Get the sum of all 'count' nodes from http://py4e-data.dr-chuck.net/comments_1719974.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

counts = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xml = urllib.request.urlopen(url, context=ctx).read() # get all the web data

# parse xml using ElementTree
tree = ET.fromstring(xml)

# move into the 'comment' nodes and save it into a list
lst = tree.findall('.//comment')

print("The length of all comment nodes:", len(lst))

for item in lst:
    counts += int(item.find("count").text)

print(counts)