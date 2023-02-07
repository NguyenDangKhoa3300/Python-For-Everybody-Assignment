# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:17:39 2023

@author: mrpot
"""

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()  # must create! Do a lot of things with cursor to work with db

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    email = line.split() # This will only get the email
    domain = email[1].split('@') # You need to count the organization, the part after '@' in email
    org = domain[1] 
    # print(org)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) # ? is a placeholder, it will add each org to ?; (org,) is a tuple with 1 value
    row = cur.fetchone() # The method is also used when we want to use the cursor() method for the iteration. This method increments the position of the cursor by 1 and after which it returns the next row.
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
