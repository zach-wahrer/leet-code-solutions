'''
Psudocode:
Make copy of sorted list
Iterate over sorted list
    Check L and R
        When there is a match for both, stop
Subtract to find difference
Return difference
'''

import unittest


def shortest_subarray(nums: list) -> int:
    sorted_list = sorted(nums)
    left = 0
    right = len(nums) - 1
    if right < 1:  # Blank input edge case
        return 0
    while nums[left] == sorted_list[left]:
        left += 1
        if left == right:  # List is already sorted edge case
            return 0

    while nums[right] == sorted_list[right]:
        right -= 1

    return right - left + 1


# 1, 2, 3, 6, 5, 4, 7, 8, 9
# 1, 2, 3, 4, 5, 6, 7, 8, 9
# 3 --- 5

# 2, 6, 4, 8, 10, 9, 15
# 2, 4, 6, 8, 9, 10, 15
# 1 --- 6

# 1, 9, 18, 64, 32
# 1, 9, 18, 32, 64
# 2 ---- 4


class TestShortestSubarray(unittest.TestCase):

    def test_264810915(self):
        input = shortest_subarray([2, 6, 4, 8, 10, 9, 15])
        output = 5
        self.assertEqual(input, output)

    def test_19186432(self):
        input = shortest_subarray([1, 9, 18, 64, 32])
        output = 2
        self.assertEqual(input, output)

    def test_987654(self):
        input = shortest_subarray([9, 7, 8, 7, 6, 5, 4])
        output = 7
        self.assertEqual(input, output)

    def test_123654789(self):
        input = shortest_subarray([1, 2, 3, 6, 5, 4, 7, 8, 9])
        output = 3
        self.assertEqual(input, output)

    def test_1234(self):
        input = shortest_subarray([1, 2, 3, 4])
        output = 0
        self.assertEqual(input, output)

    def test_1(self):
        input = shortest_subarray([1])
        output = 0
        self.assertEqual(input, output)

    def test_blank(self):
        input = shortest_subarray([])
        output = 0
        self.assertEqual(input, output)

    def test_21(self):
        input = shortest_subarray([2, 1])
        output = 2
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
