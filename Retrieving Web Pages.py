# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:13:07 2023

@author: mrpot
"""

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)