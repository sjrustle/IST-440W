__author__ = 'Scott'

import logging
import web
import ebayFinder
from Kerb_Auth_Check import auth_kinit,does_ticket_exist
##import SQLConnection
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types

logging.basicConfig(filename="service.log", level="DEBUG")

urls = ("/ebay", "EbayServ",
        "/ebay.wsdl", "EbayServ",
        "/","Hello"
        )
render = web.template.Template("$def with (var)\n$:var")

class SoapService(SimpleWSGISoapApp):
    """Class for webservice """
    ##Login method
    @soapmethod(soap_types.String, soap_types.String, _returns=soap_types.Boolean)
    def service_login(self,username, password):
        logging.info("Login attempted") ## add date
        if auth_kinit(username, password) == True:
            return
        return

    #if does_ticket_exist() == True:
    # @soapmethod(soap_types.String, _returns=soap_types.String)
    # def ebay_service(self,keyword):
    #     return ebayFinder.itemFinder(keyword)

##Methods here are for how web service communicates
class EbayServ(SoapService):
    """Class for web.py """
    def start_response(self, status, headers):
        web.ctx.status = status
        for header, value in headers:
            web.header(header, value)

    def GET(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))

    ##Primary method
    def POST(self):
        response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
        return render("\n".join(response))

##potential front page the rest is backend API
class Hello():
    def GET(self):
        return render


app=web.application(urls, globals())

if __name__ == "__main__":
    app.run()