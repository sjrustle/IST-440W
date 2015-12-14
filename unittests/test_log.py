# Shows system path
import unittest
import sys
sys.path.append('..')
import wsLogging
import logging

class TestKerbAuthCheck(unittest.TestCase):
    def test_logger_create(self):
        logger = logging.getLogger('Tests')
        log = wsLogging.logger_create("UnitTest")
        self.assertTrue(log)

    def test_error_logging_create(self):
        log = wsLogging.error_logging("UnitTest","Something")
        self.assertFalse(log)

    def test_audit_logger_create(self):
        log = wsLogging.audit_logging("UnitTest","audit")
        self.assertFalse(log)





if __name__ == '__main__':
    unittest.main(exit = False)