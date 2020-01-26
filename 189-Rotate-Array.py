'''
Psudocode:

'''

import unittest


def rotate_array(nums: list, k: int) -> None:
    pass


class TestRotateArray(unittest.TestCase):

    def test_1234567_3(self):
        input = rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
        output = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(input, output)

    def test_12_1(self):
        input = rotate_array([1, 2], 1)
        output = [2, 1]
        self.assertEqual(input, output)

    def test_1_1(self):
        input = rotate_array([1], 1)
        output = [1]
        self.assertEqual(input, output)

    def test_blank(self):
        input = rotate_array([], 0)
        output = []
        self.assertEqual(input, output)

    def test_123_2(self):
        input = rotate_array([1, 2, 3], 2)
        output = [3, 1, 2]
        self.assertEqual(input, output)

    if __name__ == "__main__":
        unittest.main()
