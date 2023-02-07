# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:09:46 2023

@author: mrpot
"""

import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = '')

mysocket.close()

# To open developer tools on web browser, press Ctrl + Shift + I