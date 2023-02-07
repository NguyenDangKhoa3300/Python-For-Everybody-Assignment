# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:41:57 2023

@author: mrpot
"""

fname = input("Enter file: ")
fh = open(fname)
final_list = []
counts = dict()
for line in fh:
    if not line.startswith("From"):
        continue
    x = line.split()
    if len(x)  == 7:
        x = x[1]
        final_list.append(x)

print(final_list)

for i in final_list:
    counts[i] = counts.get(i, 0) + 1
    #print(counts)

big_words = None
big_counts = None
for words, counts in counts.items():
    if big_counts == None or counts > big_counts:
        big_words = words
        big_counts = counts

print(big_words, big_counts)
