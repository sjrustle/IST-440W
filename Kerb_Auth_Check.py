
import os
from subprocess import Popen, PIPE
import re
from wsLogging import error_logging, audit_logging

def auth_kinit (username, password):
	auth = Popen(['kinit', username], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	auth.stdin.write('%s\n' % password)
	auth.wait()
	return does_ticket_exist(username)

def does_ticket_exist(username):
    # Sets the path
    path = '/tmp'
    a = False

    try:
        # Get list of items in the path
        for i in os.listdir(path):
            if a == True:
                break
            # Change the working directory to the path
            os.chdir(path)
            # File and directory check
            if os.path.isdir(i):
                continue
            if os.path.isfile(i):
                # Open the file
                hand = open(i)
                # Search for username
                for line in hand:
                    if re.search(username,line):
                        a = True
                        break
                    else:
                        continue
    except IOError, e:
        error_logging("Kerb_Auth_Check", e)
    except Exception, e:
        error_logging("Kerb_Auth_Check", e)
    return a


a = does_ticket_exist("bkt5031")

print a


