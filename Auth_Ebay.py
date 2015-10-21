__author__ = 'Scott'
import subprocess

def authorized_user():
    if subprocess.call(["kinit"]):
        print "That worked"

authorized_user()
##THIS IS A CHECK

