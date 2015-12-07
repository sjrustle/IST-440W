import unittest
import Kerb_Auth_Check

class KerbUnitTest(unittest):

    # Does kerbose find a ticket if created
    def auth_kinit_true:
        Kerb_Auth_Check.does_ticket_exist()

    # Does Kerberose deny the user if the ticket doens't exist
