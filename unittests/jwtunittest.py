import Create_Token
import unittest
import CRUD

# Shows system path
import sys
sys.path.append('/home/sjr5249/MyRepo/IST-440W')

class JsonTokenUnitTest(unittest):

    def test_con_create_json(self):
        con = Create_Token.create_connection()
        self.assertTrue(con)

    # def test_json_ticket_return(self):
    #     jwt = Create_Token.return_jwt()


a = JsonTokenUnitTest.test_con_create_json()
print a