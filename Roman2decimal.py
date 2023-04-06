import unittest

def roman_to_decimal_uno(roman):
    return 1
def roman_to_decimal_dos(roman):
    return 2 
def roman_to_decimal_tres(roman):
    return 3

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal_uno('I')
        self.assertEqual(resultado, 1)
    def test_II(self):
        resultado = roman_to_decimal_dos('II')
        self.assertEqual(resultado, 2)
    def test_III(self):
        resultado = roman_to_decimal_tres('III')
        self.assertEqual(resultado, 3)

if __name__ == '__main__':
    unittest.main()