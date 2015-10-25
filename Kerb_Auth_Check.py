import subprocess
from subprocess import Popen, PIPE

def auth_kinit (username, password):
	auth = Popen(['kinit', username], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	auth.stdin.write('%s\n' % password)
	auth.wait()
	return does_ticket_exist()

def does_ticket_exist():
    	if subprocess.call(['klist', '-s']) == 0: ## needs to be changed to use grep to match username and ticket name
            return True
        else:
            return False



print does_ticket_exist()


