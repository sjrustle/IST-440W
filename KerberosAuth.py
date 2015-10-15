#!/usr/bin/python

import subprocess 

if subprocess.call(['klist','-s']) == 0:  
 print "Credentials Exist" 

else: 
 print "No Credentials Exists"
 exit()



