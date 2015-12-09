__author__ = 'Scott'

#Team/Group imports

import ebayFinder
from Kerb_Auth_Check import auth_kinit
from Create_Token import return_jwt
import logging
import web
from wsLogging import error_logging, audit_logging
import ConEng
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
        # TODO: Currenly making one call should be multiple calls, meaning that username,passwrod, and search is sent here
        @soapmethod(soap_types.String, soap_types.String, soap_types.String, _returns=soap_types.String)
        def service_login(self,username, password,search):

            if auth_kinit(username, password) == True:
                audit_logging("webService", "Login successful")
                #Send Json token with permissions
                service_type = return_jwt(username)
                if service_type == 1:
                    # TODO:RabbitMQ Goes here
                    #return ConEng.runtest(search)
                    print "Returned a 1"

            else:
                audit_logging("webService", "Login Failed")
                #Send message with failure
                return "Failed to connect to service"
    except TypeError, e:
        error_logging("webService", e)
    except:
        error_logging("webService", "Failed")

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


