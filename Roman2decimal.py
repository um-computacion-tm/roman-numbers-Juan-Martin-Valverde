import unittest
def roman_to_decimal(num):
    roman_a_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    newNum = 0
    
    for numeral in num:
        oldNum = roman_a_decimal[numeral]
        decimal += oldNum
        
        if newNum < oldNum:
            decimal -= 2 * newNum
        
        newNum = oldNum

    return decimal

def test_I(self):
    resultado = roman_to_decimal('I')
    self.assertEqual(resultado, 1)

def test_II(self):
    resultado = roman_to_decimal('II')
    self.assertEqual(resultado, 2)

def test_III(self):
    resultado = roman_to_decimal('III')
    self.assertEqual(resultado, 3)

def test_V(self):
    resultado = roman_to_decimal('V')
    self.assertEqual(resultado, 5)

def test_X(self):
    resultado = roman_to_decimal("X")
    self.assertEqual(resultado, 10)

def test_VI(self):
    resultado = roman_to_decimal('VI')
    self.assertEqual(resultado, 6)

def test_VII(self):
    resultado = roman_to_decimal('VII')
    self.assertEqual(resultado, 7)

def test_IV(self):
    resultado = roman_to_decimal('IV')
    self.assertEqual(resultado, 4)

def test_IX(self):
    resultado = roman_to_decimal('IX')
    self.assertEqual(resultado, 9)

def test_XI(self):
    resultado = roman_to_decimal('XI')
    self.assertEqual(resultado, 11)

def test_XIV(self):
    resultado = roman_to_decimal('XIV')
    self.assertEqual(resultado, 14)
    
def test_CDXLIV(self):
    resultado = roman_to_decimal('CDXLIV')
    self.assertEqual(resultado, 444)
    
def test_DCLXVI(self):
    resultado = roman_to_decimal('DCLXVI')
    self.assertEqual(resultado, 666)


if __name__ == '__main__':
     unittest.main()
