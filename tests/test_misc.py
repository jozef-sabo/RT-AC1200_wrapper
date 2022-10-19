import unittest
from rt_ac1200_wrapper import misc as misc


class Tests(unittest.TestCase):
    def test_check_ip(self) -> None:
        self.assertTrue(misc.check_ip("192.168.1.1"))
        self.assertTrue(misc.check_ip("0.0.0.0"))
        self.assertTrue(misc.check_ip("1.1.0.0"))
        self.assertTrue(misc.check_ip("255.255.255.255"))
        self.assertFalse(misc.check_ip("256.255.255.255"))
        self.assertFalse(misc.check_ip("255.256.255.255"))
        self.assertFalse(misc.check_ip("255.256.256.255"))
        self.assertFalse(misc.check_ip("255.255.255.256"))
        self.assertFalse(misc.check_ip("255.255.255"))
        self.assertFalse(misc.check_ip("255.255"))
        self.assertFalse(misc.check_ip("a"))
        self.assertFalse(misc.check_ip("localhost"))
