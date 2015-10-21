__author__ = 'Scott'
import subprocess

def authorized_user():
    if subprocess.call(["kinit"]):
        return "That worked"

