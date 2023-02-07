# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:47:20 2023

@author: mrpot
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break


    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num
    elif largest < num:
        largest = num

    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num


print("Maximum is", largest)
print("Minimum is", smallest)

# =============================================================================
# list_number = []
# 
# list_length = input("Enter list length: ")
# 
# try:
#     l = int(list_length)
# except:
#     print("Invalid value")
# 
# for x in range(l):
#     item = input("Enter number: ")
#     try:
#         i = int(item)
#     except:
#         print("Invalid value")
#         break
#     
#     list_number.append(i)
#     
# print("Maximum: ", max(list_number))
# print("Minimum: ", min(list_number))
# =============================================================================
