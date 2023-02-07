# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:32:11 2023

@author: mrpot
"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line.find("0")
    number = line[x:]
    number = float(number)
    print(number)
    count += 1
    total = total + number
        
average = total / count    
print("Average spam confidence:", average)