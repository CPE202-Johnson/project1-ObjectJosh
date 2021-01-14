import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    # test: True case
    def test_bear_01(self):
        self.assertTrue(bears(250))

    # test: True case -> starting number is 42
    def test_bear_02(self):
        self.assertTrue(bears(42))
    
    # test: False case
    def test_bear_03(self):
        self.assertFalse(bears(53))

    # test: False case
    def test_bear_04(self):
        self.assertFalse(bears(43))

    # test: False case -> number lower than 42
    def test_bear_05(self):
        self.assertFalse(bears(2))
    
    # test: False case -> number lower than 42
    def test_bear_06(self):
        self.assertFalse(bears(41))
    
    # test: False case -> number is 0
    def test_bear_07(self):
        self.assertFalse(bears(0))

    # test: False case -> number is negative
    def test_bear_08(self):
        self.assertFalse(bears(-3))

if __name__ == "__main__":
    unittest.main()
