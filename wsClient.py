__author__ = 'Scott'
import getpass
import jwt
from soaplib.client import make_service_client
from webService import EbayServ

#client
try:
    client = make_service_client('http://localhost:8080/ebay',EbayServ())

    # Try to connect to client and get json token
    json = client.service_login("bkt5031", "H464Jd$")

    # Json sent back, with permissions decode
    decode = jwt.decode(json,'secret', algorithm='HS256')

    # Get message from rabbitmq
    # if decode.value(0) == 1:
    #     # Has permissions for ebay, will do the ebay call here
    #     print "User has permission"
    # else:
    #     # User does not have permission
    #     print "User does not have permission"

except:
    print "Login Failed"
