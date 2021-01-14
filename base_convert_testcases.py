import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self): # base 2
        self.assertEqual(convert(45, 2),"101101")

    def test_base4(self): # test: base 4
        self.assertEqual(convert(30, 4),"132")

    def test_base16(self): # test: base 16
        self.assertEqual(convert(316, 16),"13C")
    
    def test_base16_2(self): # test: base 16 -> large number, all letter output
        self.assertEqual(convert(11259375, 16), "ABCDEF")
    
    def test_base16_3(self): # test: base 16 -> when base and number are same
        self.assertEqual(convert(16, 16), "10")
    
    def test_base16_4(self): # test: base 16 -> base is directly divisible by number
        self.assertEqual(convert(160 ,16), "A0")
    
    def test_base2_2(self): # test: base 2 -> output is 0 as a string
        self.assertEqual(convert(0, 2), "0")

if __name__ == "__main__":
    unittest.main()
