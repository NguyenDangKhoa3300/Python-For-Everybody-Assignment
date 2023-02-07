# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 00:15:34 2023

@author: mrpot
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Lấy link ở vị trí thứ n -> đọc link đó -> lập lại y lần -> kết quả là link ở vị trí n lần thứ  
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

lst = list()
url_lst = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input("Enter position: ")) - 1
process_time = int(input("How many times do you want to process: "))

for i in range(process_time):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    taglist = list()
    for tag in tags:
        x = tag.get('href', None)
        taglist.append(x)
    
    url = taglist[position]
    url_lst.append(url) # optional, just to find last url directly
    print("Retrieving:", url)

print("****\nLast URL:", url_lst[-1])


# =============================================================================
# position = input("Enter position: ")
# process_time = input("How many times do you want to process: ")
# process_time = int(process_time)
# start = 0
# 
# while start < process_time:
#     new_html = urllib.request.urlopen(lst[int(position) - 1], context=ctx).read()
#     new_soup = BeautifulSoup(new_html, 'html.parser')
#     
#     tags1 = soup('a')
#     for tag1 in tags1:
#         y = tag1.get('href', None)
#         new_lst.append(y)
#     
#     print("Retrieving:", new_lst[int(position)])
#     start += 1
# 
# =============================================================================
# TEST SPACE

