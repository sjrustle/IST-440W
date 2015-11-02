import subprocess
from subprocess import Popen, PIPE

def auth_kinit (username, password):
	auth = Popen(['kinit', username], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	auth.stdin.write('%s\n' % password)
	auth.wait()
	return does_ticket_exist(username)

def does_ticket_exist(username):
    Popen(['cd','/'])
    a = Popen(['grep', username, "/tmp"]).communicate()
    if a > 0:
        return True
    else:
        return False



#print does_ticket_exist()


