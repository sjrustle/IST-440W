__author__ = 'Scott'
import getpass
import jwt
from soaplib.client import make_service_client
from webService import EbayServ

#client
try:
    client = make_service_client('http://localhost:8080/ebay',EbayServ())
except:
    print "Client failed"

try:
    # Try to connect to client and get json token
    json = client.service_login("bkt5031", "H464Jd$")

    # Json sent back, with permissions decode
    decode = jwt.decode(json,'secret', algorithm='HS256')
    # Get message from rabbitmq
except:
    print "Login Failed"
