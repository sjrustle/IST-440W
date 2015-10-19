#!/usr/bin/python 

import MySQLdb

db = MySQLdb.connect(host="localhost",

user="root",
passwd="Team5",
db="testDB")

print ("Database Found") 

cur = db.cursor()

print db


column = raw_input("> ")
values = raw_input("> ")
create = ("INSERT INTO user {} Values ( '{}')".format(column,values))

cur.execute(create)

db.commit()

cur.close()
db.close()

