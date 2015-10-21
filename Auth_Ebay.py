__author__ = 'Scott'
import subprocess
import ebayFinder

def authorized_user(keyword):
    if subprocess.call(["kinit"]) == 0:
        print "That worked"
        ebayFinder.itemFinder(keyword)
    else:
        print "Fail"
    ##print "The Function Ran"

##THIS IS A CHECK, SOmething

