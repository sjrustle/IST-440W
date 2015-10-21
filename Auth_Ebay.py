__author__ = 'Scott'
import subprocess

def authorized_user():
    subprocess.call(["kinit"])
