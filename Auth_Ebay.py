__author__ = 'Scott'
import subprocess

def authorized_user():
    if subprocess.call(["kinit"]) == 0:
        print "That worked"
    else:
        print "Fail"
    print "The Function Ran"

authorized_user()
##THIS IS A CHECK, SOmething

