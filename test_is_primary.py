import unittest

from is_primary import is_primary

class TestIsPrimary(unittest.TestCase):

    def test_two(self):
        self.assertTrue(is_primary(2))

    def test_three(self):
        self.assertTrue(is_primary(3))

    def test_four(self):
        self.assertFalse(is_primary(4))

    def test_five(self):
        self.assertTrue(is_primary(5))

    def test_nine(self):
        self.assertFalse(is_primary(9))

