__author__ = 'Scott'

#Team/Group imports
import datetime
import ebayFinder
from Kerb_Auth_Check import auth_kinit
import logging
import web
from wsLogging import start_logging
##import SQLConnection

#WebPy imports
from soaplib.wsgi_soap import SimpleWSGISoapApp
from soaplib.service import soapmethod
from soaplib.serializers import primitive as soap_types


urls = ("/ebay", "EbayServ",
        "/ebay.wsdl", "EbayServ",
        )
render = web.template.Template("$def with (var)\n$:var")

##Processing and login is in the class
class SoapService(SimpleWSGISoapApp):
    """Class for webservice """
    ##Login method
    try:
        @soapmethod(soap_types.String, soap_types.String, _returns=soap_types.Boolean)
        def service_login(self,username, password):
           # logging.info("Login attempted {}",datetime.datetime.now())
            if auth_kinit(username, password) == True:
                start_logging("webService")
            else:
                start_logging("webService")
                return False
    except TypeError:
        start_logging("webService")
    except:
        start_logging("webService")


    #if does_ticket_exist() == True:
    # @soapmethod(soap_types.String, _returns=soap_types.String)
    # def ebay_service(self,keyword):
    #     return ebayFinder.itemFinder(keyword)

#Methods here are for how web service communicates
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


#Tells web app to start, gives urls
app=web.application(urls, globals())

if __name__ == "__main__":
    app.run()
    start_logging("webService")

