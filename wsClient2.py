__author__ = 'Scott'
import getpass
import jwt
from soaplib.client import make_service_client
from webService import EbayServ
import rabbit_receive
import runpy

#client
try:
    client = make_service_client('http://localhost:8080/ebay',EbayServ())
    name = raw_input("Enter username: ")
    password = raw_input("Enter password: ")
    search = raw_input("What do you want to find ? ")
    intensity = int(raw_input("How many pages would you like ot search? "))
    day_to_use = raw_input("What would you like to estimate the price for? ")

    # Try to connect to client and get json token
    json = client.service_login(name, "H464Jd$",search)
    # Json sent back, with permissions decode
    decode = jwt.decode(json,'secret', algorithm='HS256')
    service_type = decode.get('user_service')

    if service_type == 1:
        # Has permissions for ebay, will do the ebay call here
        result = client.prediction(search,intensity,day_to_use)
        print result
        get_rabbit_mq = raw_input()
        if get_rabbit_mq == 'yes':
            try:
                rabbit_receive.start_consume()
            except:
                print "runpy error"
    else:
         # User does not have permission
         print "User does not have permission"
except:
    print "Login Failed"
