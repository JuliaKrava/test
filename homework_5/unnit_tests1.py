import unittest
from homework_5.unnit_test import is_year_leap

class IsYearLeapTests(unittest.TestCase):
    def test_1(self):
        res = is_year_leap(2000)
        self.assertTrue(res)

    def test_2(self):
        res = is_year_leap(2001)
        self.assertFalse(res)

    def test_3(self):
        res = is_year_leap(2400)
        self.assertTrue(res)

    def test_4(self):
        res = is_year_leap(1997)
        self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()


