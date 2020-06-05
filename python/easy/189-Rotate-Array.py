'''
Psudocode:

'''

import unittest


# Brute O(n*k)
def rotate_array_brute(nums: list, k: int) -> None:
    for i in range(k):
        nums.insert(0, nums[-1])
        nums.pop(-1)
    return nums


# O(n) solution
def rotate_array(nums: list, k: int) -> None:
    if k > 0:
        k %= len(nums)
    if k != 0:
        move_group_size = len(nums) - k
        new_left = nums[move_group_size:]
        new_right = nums[:move_group_size]
        for i, num in enumerate(new_left):
            nums[i] = num
        for i, num in enumerate(new_right):
            nums[i + k] = num
    return nums


class TestRotateArray(unittest.TestCase):

    def test_1234567_3(self):
        input = rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
        output = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(input, output)

    def test_12_1(self):
        input = rotate_array([1, 2], 2)
        output = [1, 2]
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

    def test_k_bigger_than_len(self):
        input = rotate_array([3, 4, 3], 6)
        output = [3, 4, 3]
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
