#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost",

user="root",
passwd="Team5",
db="TestDB")
cur = db.cursor()
print db

cur.execute("SELECT * FROM Users")

for row in cur.fetchall() : 
    print row[0] 
