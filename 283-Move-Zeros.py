'''
Psudocode:
    Brute:
    Iterate through the loop in place
    If we find a 0, delete that element, increment a counter
    When we get to the end, add counter's worth of 0s.
'''

import unittest


# O(n^2) - Fails some cases
def move_zeros_brute(nums: list) -> None:
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)
    return nums


# O(n)
def move_zeros(nums: list) -> None:
    # Length 2 edge case
    if len(nums) == 2:
        if nums[0] == 0:
            nums[0] = nums[1]
            nums[1] = 0

    pointer1 = 0
    pointer2 = 1
    while pointer2 < len(nums) - 1:
        if nums[pointer1] == 0:
            while nums[pointer2] == 0:
                pointer2 += 1
                if pointer2 == len(nums) - 1:
                    break
            nums[pointer1] = nums[pointer2]
            nums[pointer2] = 0
        else:
            pointer2 += 1
        pointer1 += 1
    # Length of 3 edge cases
    if len(nums) > 2 and nums[pointer1] == 0:
        nums[pointer1] = nums[pointer2]
        nums[pointer2] = 0

    return nums


class TestMoveZeros(unittest.TestCase):

    def test_010312(self):
        input = move_zeros([0, 1, 0, 3, 12])
        output = [1, 3, 12, 0, 0]
        self.assertEqual(input, output)

    def test_blank(self):
        input = move_zeros([])
        output = []
        self.assertEqual(input, output)

    def test_01(self):
        input = move_zeros([0, 1])
        output = [1, 0]
        self.assertEqual(input, output)

    def test_1(self):
        input = move_zeros([1])
        output = [1]
        self.assertEqual(input, output)

    def test_456000(self):
        input = move_zeros([4, 5, 6, 0, 0, 0])
        output = [4, 5, 6, 0, 0, 0]
        self.assertEqual(input, output)

    def test_90909099(self):
        input = move_zeros([9, 0, 9, 0, 9, 0, 9, 9])
        output = [9, 9, 9, 9, 9, 0, 0, 0]
        self.assertEqual(input, output)

    def test_001(self):
        input = move_zeros([0, 0, 1])
        output = [1, 0, 0]
        self.assertEqual(input, output)

    def test_0001(self):
        input = move_zeros([0, 0, 0, 1])
        output = [1, 0, 0, 0]
        self.assertEqual(input, output)

    def test_101(self):
        input = move_zeros([1, 0, 1])
        output = [1, 1, 0]
        self.assertEqual(input, output)

    def test_111(self):
        input = move_zeros([1, 1, 1])
        output = [1, 1, 1]
        self.assertEqual(input, output)

    def test_011(self):
        input = move_zeros([0, 1, 1])
        output = [1, 1, 0]
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
