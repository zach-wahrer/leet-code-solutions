'''
Psudocode:

'''

import unittest


def unique_ints(numbers: int) -> list:
    return [1, 1]


class TestUniqueList(unittest.TestCase):

    def test_5(self):
        input = sum(unique_ints(5))
        output = 0
        self.assertEqual(input, output)

    def test_3(self):
        input = sum(unique_ints(3))
        output = 0
        self.assertEqual(input, output)

    def test_1(self):
        input = sum(unique_ints(1))
        output = 0
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
