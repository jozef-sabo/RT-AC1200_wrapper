import unittest
from rt_ac1200_wrapper import AC1200_router


class Tests(unittest.TestCase):
    def test_AC1200_router_class(self) -> None:
        self.assertTrue(AC1200_router("192.168.1.1"))
        self.assertTrue(AC1200_router("192.168.1.1", 1))
        self.assertTrue(AC1200_router("192.168.1.1", 65535))
        self.assertTrue(AC1200_router("localhost"))

        with self.assertRaises(ValueError):
            AC1200_router("256.255.255.0")

        with self.assertRaises(AssertionError):
            AC1200_router("192.168.1.1", 0)
        with self.assertRaises(AssertionError):
            AC1200_router("192.168.1.1", 65536)
        with self.assertRaises(AssertionError):
            AC1200_router("192.168.1.1", -1)



