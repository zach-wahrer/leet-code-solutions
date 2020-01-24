'''
Psudocode:
    Loop through range(len(list))
        If i not in list
            Append new list
    Return new list
'''

import unittest


def missing_nums(nums: list) -> list:
    pass


class TestMissingNums(unittest.TestCase):

    def test_43278231(self):
        input = missing_nums([4, 3, 2, 7, 8, 2, 3, 1])
        output = [5, 6]
        self.assertEqual(input, output)

    def test_1456910(self):
        input = missing_nums([1, 4, 5, 6, 9, 10])
        output = [2, 3, 7, 8]
        self.assertEqual(input, output)

    def test_23458(self):
        input = missing_nums([2, 3, 4, 5, 8])
        output = [1, 6, 7]
        self.assertEqual(input, output)

    def test_1234567888(self):
        input = missing_nums([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9])
        output = [10, 11]
        self.assertEqual(input, output)

    def test_123344579(self):
        input = missing_nums([1, 2, 3, 3, 4, 4, 5, 7, 9])
        output = [6, 8]
        self.assertEqual(input, output)
