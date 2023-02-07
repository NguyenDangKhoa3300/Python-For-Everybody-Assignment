# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:55:26 2023

@author: mrpot
"""

text = "X-DSPAM-Confidence:    0.8475"

x = text.find("0")
y = float(x)
z = int(y)
print(text[z:])

