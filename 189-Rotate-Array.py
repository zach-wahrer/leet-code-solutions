'''
Psudocode:

'''

import unittest


# Brute O(n^2)
def rotate_array(nums: list, k: int) -> None:
    for i in range(k):
        nums.insert(0, nums[-1])
        nums.pop(-1)
    return nums


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
        output = [2, 3, 1]
        self.assertEqual(input, output)

    def test_negatives(self):
        input = rotate_array([-1, -100, 3, 99], 2)
        output = [3, 99, -1, -100]
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
