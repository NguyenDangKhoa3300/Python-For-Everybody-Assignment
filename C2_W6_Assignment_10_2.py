# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:10:34 2023

@author: mrpot
"""

fname = input("Enter a file: ")
handle = open(fname)
new_lst = []
final_lst = []
counts = dict()
for line in handle:
    if not line.startswith("From"):
        continue
    temp = line.split()
    if len(temp) == 7: # length of the list
        new_lst = temp[5].split(":")
        final_lst.append(new_lst[0])

#print(final_lst)

# counts for dictionary
for i in final_lst:
    counts[i] = counts.get(i, 0) + 1

# bring into tuples
temp_lst = []
for k, v in counts.items():
    newtup = (k, v)
    temp_lst.append(newtup)

temp_lst = sorted(temp_lst)

for k,v in temp_lst:
    print(k, v)

    
            