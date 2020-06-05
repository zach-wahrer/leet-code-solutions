"""
Psudocode:

"""

import unittest


def to_lower(str):

    return str.lower()


class TestLower(unittest.TestCase):

    def test_Hello(self):
        input = to_lower("Hello")
        output = "hello"
        self.assertEqual(input, output)

    def test_here(self):
        input = to_lower("here")
        output = "here"
        self.assertEqual(input, output)

    def test_LOVELY(self):
        input = to_lower("LOVELY")
        output = "lovely"
        self.assertEqual(input, output)

    def test_RaGe(self):
        input = to_lower("RaGe")
        output = "rage"
        self.assertEqual(input, output)

    def test_MelloW(self):
        input = to_lower("MelloW")
        output = "mellow"
        self.assertEqual(input, output)

    def test_uh0H1(self):
        input = to_lower("uh0H1")
        output = "uh0h1"
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
