#!/usr/bin/python

import MySQLdb


con = lite.connect('test.db')
with con:    
  cur = con.cursor()    
  cur.execute("SELECT * FROM Cars") 
  rows = cur.fetchall() 
  for row in rows:
      print row
