__author__ = 'Scott'
import getpass
import jwt
from soaplib.client import make_service_client
from webService import EbayServ

#client
try:
    client = make_service_client('http://localhost:8080/ebay',EbayServ())

    # Try to connect to client and get json token
    json = client.service_login("bkt5031", "H464Jd$","Play Station")
    print json
    # Json sent back, with permissions decode
    decode = jwt.decode(json,'secret', algorithm='HS256')
    print decode
    print type(decode)
    service_type = decode.get('user_service')
    print service_type

    if service_type == 1:
        # Has permissions for ebay, will do the ebay call here
        print "User has permissions"
        result = client.prediction("Xbox One")
        print result
    else:
         # User does not have permission
         print "User does not have permission"
except:
    print "Login Failed"
