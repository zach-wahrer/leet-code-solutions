'''
Psudocode:

'''

import unittest
import math


def square_root(x: int) -> int:
    return int(x ** 0.5)
    # return int(math.sqrt(x))


class TestSquareRoot(unittest.TestCase):

    def test_4(self):
        input = square_root(4)
        output = 2
        self.assertEqual(input, output)

    def test_8(self):
        input = square_root(8)
        output = 2
        self.assertEqual(input, output)

    def test_99(self):
        input = square_root(99)
        output = 9
        self.assertEqual(input, output)

    def test_14cubed(self):
        input = square_root(14**4)
        output = 196
        self.assertEqual(input, output)

    def test_0(self):
        input = square_root(0)
        output = 0
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
