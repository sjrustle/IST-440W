__author__ = 'Scott'
import getpass
from soaplib.client import make_service_client
from webService import EbayServ

#client
try:
    client = make_service_client('http://localhost:8080/ebay',EbayServ())
except:
    #Print statment for now, but will change in last version
    print "Client failed"

try:
    user_name = str(raw_input("> Enter user: "))
    blatant_password = str(getpass.getpass("> Enter your password: "))
    if client.service_login(user_name, blatant_password):
        #Add logging here
        print("Login success.")
    else:
        #Add logging here
        print("Login Fail, try again.")
## exceptions here will log back to the server
except TypeError as e:
    #Ask Joe how to handle logs from the client
    print e