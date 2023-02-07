# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:15:10 2023

@author: mrpot
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, "rt")
for line in fh:
    line = line.rstrip()
    x = line.upper()
    print(x)

