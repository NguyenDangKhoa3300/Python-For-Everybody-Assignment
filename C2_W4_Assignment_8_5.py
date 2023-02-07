# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:29:24 2023

@author: mrpot
"""

fname = input("Enter a file: ")
handle = open(fname)
lst = list()
counts = 0

for line in handle:
    if not line.startswith("From"):
        continue
    lst = line.split()
    if len(lst) == 7: # depends on requirements only get this string like "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
        print(lst[1])
        counts += 1
                
print("There were", counts, "lines in the file with From as the first word")

