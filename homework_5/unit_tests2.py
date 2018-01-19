import unittest
from homework_5.treugol import treugolnik

class TreTest (unittest.TestCase):
    def test_one(self):
        self.assertTrue(treugolnik(2,3,4))

    def test_two(self):
        self.assertFalse(treugolnik(5,6,26))

    def test_three(self):
        self.assertTrue(treugolnik(7,6,12))

if __name__ == '__main__':
    unittest.main()