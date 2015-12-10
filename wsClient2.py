__author__ = 'Scott'
import getpass
import jwt
from soaplib.client import make_service_client
from webService import EbayServ
import rabbit_receive

#client
try:
    client = make_service_client('http://localhost:8080/ebay',EbayServ())
    name = raw_input("Enter username: ")
    password = raw_input("Enter password: ")
    search = raw_input("What do you want to find ?")

    # Try to connect to client and get json token
    json = client.service_login(name, "H464Jd$",search)
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
        result = client.prediction(search)
        print result
        try:
            rabbit_receive.callback('FirstQ')
        except:
            print "RabbitMQ failed"

    else:
         # User does not have permission
         print "User does not have permission"
except:
    print "Login Failed"
