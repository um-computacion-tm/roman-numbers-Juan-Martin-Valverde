import unittest
from my_romanos import decimal2roman 
class Mytest(unittest.TestCase):
    def test_I (self):
        self.essertEqual (decimal2roman(1),'i')

if __name__== '__main__':
    unittest.main()