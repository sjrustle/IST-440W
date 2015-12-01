import Create_Token
import unittest

class JsonTokenUnitTest(unittest):

    def con_create_json(self):
        con = Create_Token.create_connection()
        self.assertEqual(con,)

    def json_ticket_return_test(self):
        jwt = Create_Token.return_jwt()