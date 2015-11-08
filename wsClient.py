__author__ = 'Scott'
import getpass
from soaplib.client import make_service_client
from webService import EbayServ

#client
try:
    client = make_service_client('http://localhost:8080/ebay',EbayServ())
except:
    print "Client failed"

try:
    client.service_login("bkt5031", "H464Jd$")

    # Json sent back, with permissions

    # Get message from rabbitmq
except:
    print "Login Failed"
