import subprocess
from subprocess import Popen, PIPE

def auth_kinit (username, password):
	auth = Popen(['kinit', username], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	auth.stdin.write('%s\n' % password)
	autht.wait()

def does_ticket_exist():
    	if subprocess.call(['klist', '-s']) == 0:
            return True
        else:
            return False



print does_ticket_exist()


