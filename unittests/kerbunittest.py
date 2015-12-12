# Shows system path
import unittest
import sys
sys.path.append('..')
import Create_Token
import CRUD
import Kerb_Auth_Check

class TestKerbAuthCheck(unittest.TestCase):
    def test_kerk_auth_check_ticket_exist(self):
        ticket = Kerb_Auth_Check.does_ticket_exist('bkt5031')
        self.assertTrue(ticket)

if __name__ == '__main__':
    unittest.main(exit = False)