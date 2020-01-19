'''
Psudocode:

'''

import unittest


def find_substring(haystack: str, needle: str) -> int:
    pass


class TestSubstring(unittest.TestCase):

    def test_hello(self):
        input = find_substring("hello", "ll")
        output = 2
        self.assertEqual(input, output)

    def test_aaaaa(self):
        input = find_substring("aaaaa", "bba")
        output = -1
        self.assertEqual(input, output)

    def test_empty(self):
        input = find_substring("emptystring", "")
        output = 0
        self.assertEqual(input, output)

    def test_long(self):
        input = find_substring("this is a very long string with spaces", "ces")
        output = 35
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
