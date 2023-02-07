# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:21:55 2023

@author: mrpot
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
final_lst = list()
for line in fh:
    x = line.rstrip()
    lst.append(x)

print(lst)

# concate list
for line in lst:
    #line.split
    stuff = line.split
    final_lst += stuff()

# removes duplicate character & sort order    
final_lst = list(dict.fromkeys(final_lst))
final_lst.sort()
print(final_lst)





    



        
    
  
    

