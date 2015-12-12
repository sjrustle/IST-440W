# Shows system path
import sys
sys.path.append('..')
import Create_Token
import unittest
import CRUD

class JsonTokenUnitTest(unittest):

    def test_con_create_json(self):
        con = Create_Token.create_connection()
        self.assertTrue(con)

    # def test_json_ticket_return(self):
    #     jwt = Create_Token.return_jwt()


if __name__ == '__main__':
    JsonTokenUnitTest.test_con_create_json()