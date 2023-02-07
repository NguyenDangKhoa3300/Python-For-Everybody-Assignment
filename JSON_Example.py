# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:54:47 2023

@author: mrpot
"""

import json

print("***EXAMPLE 1***")
data = '''
{
 "name" : "Khoa",
 "phone" : {
     "type" : "intl",
     "number" : "+846438826912"
     },
 "email" : {
     "hide" : "yes"
     }
}
'''

info = json.loads(data) # convert json to Python dictionary

print(type(info))
print("Name: ", info["name"])
print("Hide: ", info["email"]["hide"]) 
print(info["phone"])

print("***EXAMPLE 2***")
input = '''
[
 {
  "id" : "001",
  "x" : "4",
  "name" : "Khoa"
 },
 {
  "id" : "002",
  "x" : "2",
  "name" : "Yen"
 }
]
'''

info2 = json.loads(input) # convert json to Python list
print(type(info2))
print("Length of JSON list: ", len(info2))

for item in info2:
    print("Name: ", item["name"])
    print("ID: ", item["id"])
    print("Attribute: ", item["x"])