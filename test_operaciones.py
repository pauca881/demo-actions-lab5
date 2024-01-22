import unittest
from operaciones import restar
from operaciones import multiplicar
from operaciones import dividir


class TestSumar(unittest.TestCase):
 
 def test_sumar(self):
    self.assertEqual(restar(3, 2), 5)
    self.assertEqual(multiplicar(-1, 1), 0)
    self.assertEqual(dividir(-1, -1), -2)

    
if __name__ == '__main__':
 unittest.main()