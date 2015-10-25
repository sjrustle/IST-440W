__author__ = 'Scott'
import getpass
from soaplib.client import make_service_client
from webService import EbayServ

#client
client = make_service_client('http://localhost:8080/ebay',EbayServ())
user_name = raw_input("> Enter user: ")
blatant_password = getpass.getpass("> Enter your password: ")
client.service_login(user_name, blatant_password)