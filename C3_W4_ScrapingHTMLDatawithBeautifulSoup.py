# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 23:08:15 2023

@author: mrpot
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

counts = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser") # clean html by using BeautifulSoup to avoid error

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag    
    # print("Tag: ", tag)

#     print('URL:', tag.get('href', None))
    counts += int(tag.contents[0])
    
print(counts)
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)

