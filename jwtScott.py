#!/usr/bin/python

import jwt
key = 'secret'

payload = {'username':'sjr5249','password':'mypassword'}
token = jwt.encode(payload, key,'HS256')

print token

decode = jwt.decode(token, key, 'HS256')

print decode


