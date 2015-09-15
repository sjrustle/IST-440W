#!/usr/bin/python

import jwt
key = 'secret'

payload = {'username':'syq5030','password':'mypassword'}
token = jwt.encode(payload, key,'HS256')

print token

decode = jwt.decode(token, key, 'HS256')

print decode


