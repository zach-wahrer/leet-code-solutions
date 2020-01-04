'''
Psudocode:

'''

import unittest


def reverse_int(x: int) -> int:
    pass


class TestReverse(unittest.TestCase):

    def test_123(self):
        input = reverse_int(123)
        output = 321
        self.assertEqual(input, output)

    def test_minus123(self):
        input = reverse_int(-123)
        output = -321
        self.assertEqual(input, output)

    def test_120(self):
        input = reverse_int(120)
        output = 21
        self.assertEqual(input, output)

    def test_2_31(self):
        input = reverse_int(2**31)
        output = 0
        self.assertEqual(input, output)

    def test_minus2_31_minus1(self):
        input = reverse_int(-2**31 - 1)
        output = 0
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
