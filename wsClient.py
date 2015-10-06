__author__ = 'Scott'
from soaplib.client import make_service_client
from webService import EbayServ
client = make_service_client('http://localhost:8080/ebay',EbayServ())
print client.ebay_service('iPhone')