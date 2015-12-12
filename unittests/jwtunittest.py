# Shows system path
import unittest
import sys
sys.path.append('..')
import Create_Token
import CRUD

class TestJsonTokenUnit(unittest.TestCase):

    def test_con_create_json(self):
        con = Create_Token.create_connection()
        self.assertTrue(con)

    def tet_json_ticket_return(self):
        jwt = Create_Token.return_jwt("bkt5031")
        self.assertTrue(jwt)

if __name__ == '__main__':
    unittest.main(exit = False)