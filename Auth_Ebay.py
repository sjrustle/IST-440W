__author__ = 'Scott'
import subprocess

def authorized_user():
    if subprocess.call(["kinit"]) == 0:
        print "That worked"
    print "The Function Ran"

authorized_user()
##THIS IS A CHECK

