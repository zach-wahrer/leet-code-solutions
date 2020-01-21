'''
Psudocode:

'''

import unittest


def plus_one(digits: list) -> list:
    pass


class TestPlusOne(unittest.TestCase):

    def test_123(self):
        input = plus_one([1, 2, 3])
        output = [1, 2, 4]
        self.assertEqual(input, output)

    def test_0999(self):
        input = plus_one([0, 9, 9, 9])
        output = [1, 0, 0, 0]
        self.assertEqual(input, output)

    def test_1(self):
        input = plus_one([1])
        output = [2]
        self.assertEqual(input, output)

    def test_4321(self):
        input = plus_one([4, 3, 2, 1])
        output = [4, 3, 2, 2]
        self.assertEqual(input, output)


if __name__ == "main":
    unittest.main()
