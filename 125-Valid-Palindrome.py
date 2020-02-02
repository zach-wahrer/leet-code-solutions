'''
Psudocode:

'''

import unittest


def valid_palindrome(s: str) -> bool:
    pass


class TestPalindrome(unittest.TestCase):
    def test_a_man(self):
        input = valid_palindrome("A man, a plan, a canal: Panama")
        self.assertTrue(input)

    def test_radar(self):
        input = valid_palindrome("ra12dar")
        self.assertTrue(input)

    def test_radar(self):
        input = valid_palindrome("race car")
        self.assertTrue(input)

    def test_race(self):
        input = valid_palindrome("race a car")
        self.assertFalse(input)

    def test_heart(self):
        input = valid_palindrome("I heart sea food")
        self.assertFalse(input)


if __name__ == '__main__':
    unittest.main()
