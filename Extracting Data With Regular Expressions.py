# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:43:49 2023

@author: mrpot
"""
import re

fname = input("Enter a file name: ")
handle = open(fname, "rt")
text = handle.read()
counts = 0 

x = re.findall("[0-9]+", text) # find number in the text (read regular expression cheat sheet)
for i in x:
    i = int(i)
    counts += i
    
print(counts)


