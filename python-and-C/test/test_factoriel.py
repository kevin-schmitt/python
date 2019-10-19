import unittest
from numpy.ctypeslib import load_library

class TestFactoriel(unittest.TestCase):

    """ test factoriel with libray from C langage """
    def test_factoriel(self):
        numberForFact = 5
        lib = load_library('factoriel.so', '.')
        self.assertEqual(120, lib.fact(5))

if __name__ == '__main__':
    unittest.main()