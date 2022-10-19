import unittest
from rt_ac1200_wrapper import misc as misc


class Tests(unittest.TestCase):
    def test_is_ip_valid(self) -> None:
        self.assertTrue(misc.is_ip_valid("192.168.1.1"))
        self.assertTrue(misc.is_ip_valid("0.0.0.0"))
        self.assertTrue(misc.is_ip_valid("1.1.0.0"))
        self.assertTrue(misc.is_ip_valid("255.255.255.255"))
        self.assertFalse(misc.is_ip_valid("256.255.255.255"))
        self.assertFalse(misc.is_ip_valid("255.256.255.255"))
        self.assertFalse(misc.is_ip_valid("255.256.256.255"))
        self.assertFalse(misc.is_ip_valid("255.255.255.256"))
        self.assertFalse(misc.is_ip_valid("255.255.255"))
        self.assertFalse(misc.is_ip_valid("255.255"))
        self.assertFalse(misc.is_ip_valid("a"))
        self.assertFalse(misc.is_ip_valid("localhost"))

    def test_create_authorization_string(self) -> None:
        self.assertEqual(misc.create_authorization_string("", ""), "Og==")
        self.assertEqual(misc.create_authorization_string("username", "password"), "dXNlcm5hbWU6cGFzc3dvcmQ=")
        self.assertEqual(misc.create_authorization_string("username ", "password"), "dXNlcm5hbWU6cGFzc3dvcmQ=")
        self.assertEqual(misc.create_authorization_string(" username", "password"), "dXNlcm5hbWU6cGFzc3dvcmQ=")
        self.assertEqual(misc.create_authorization_string(" username ", "password"), "dXNlcm5hbWU6cGFzc3dvcmQ=")

        self.assertNotEqual(misc.create_authorization_string("username", " password"), "dXNlcm5hbWU6cGFzc3dvcmQ=")
        self.assertNotEqual(misc.create_authorization_string("username", "password "), "dXNlcm5hbWU6cGFzc3dvcmQ=")
        self.assertNotEqual(misc.create_authorization_string("username", " password "), "dXNlcm5hbWU6cGFzc3dvcmQ=")

        self.assertEqual(misc.create_authorization_string("012", "012"), "MDEyOjAxMg==")
        self.assertEqual(misc.create_authorization_string("", "a"), "OmE=")
        self.assertEqual(misc.create_authorization_string("a", ""), "YTo=")
