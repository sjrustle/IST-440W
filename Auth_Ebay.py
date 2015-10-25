__author__ = 'Scott'
import subprocess
from subprocess import Popen, PIPE
import ebayFinder

def authorized_user(keyword):
    password = keyword

    if subprocess.call(["kinit"]) == 0:
        return True
    else:
        print "Fail"
        return False
    ##print "The Function Ran"

##THIS IS A CHECK, SOmething

