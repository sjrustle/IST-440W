# Shows system path
import unittest
import sys
sys.path.append('..')
import Create_Token
import CRUD

class JsonTokenUnitTest(unittest.TestCase):

    def test_con_create_json(self):
        con = Create_Token.create_connection()
        self.assertTrue(con)

    # def test_json_ticket_return(self):
    #     jwt = Create_Token.return_jwt()


if __name__ == '__main__':
    test_instance = JsonTokenUnitTest()
    a = test_instance.test_con_create_json()
    print a