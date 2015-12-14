# Shows system path
import unittest
import sys
sys.path.append('..')
import wsLogging

class TestKerbAuthCheck(unittest.TestCase):
    def test_logger_create(self):
        log = wsLogging.logger_create("UnitTest")
        self.assertFalse(log, None)

    def test_error_logging_create(self):
        log = wsLogging.error_logging("UnitTest","Something")
        self.assertFalse(log)

    def test_audit_logger_create(self):
        log = wsLogging.audit_logging("UnitTest","audit")
        self.assertFalse(log)





if __name__ == '__main__':
    unittest.main(exit = False)