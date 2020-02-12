'''
Psudocode:
    If number is negative, return false
    If number is single digit, return true
    Convert to string, reverse, convert back to int
    Compare two numbers
'''

import unittest


def check_palindrome(x: int) -> bool:
    if x < 0:
        return False
    reversed_number = int((str(x)[::-1]))
    return reversed_number == x


class TestPalindromeCheck(unittest.TestCase):

    def test_121(self):
        self.assertTrue(check_palindrome(121))

    def test_minus121(self):
        self.assertFalse(check_palindrome(-121))

    def test_10(self):
        self.assertFalse(check_palindrome(10))

    def test_0(self):
        self.assertTrue(check_palindrome(0))

    def test_900009(self):
        self.assertTrue(check_palindrome(900009))

    def test_1234321(self):
        self.assertTrue(check_palindrome(1234321))

    def test_891224(self):
        self.assertFalse(check_palindrome(891224))


if __name__ == '__main__':
    unittest.main()
