'''
Psudocode:
    Use list.index() to find value
    If not found, iterate through list, comparing
        If value is less than first value, return 0
        If value is > current value, but < next value, return next index
        If it is greater than final value, return n+1
'''

import unittest


def search_input_pos(nums: list, target: int) -> int:
    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    else:
        for pos, i in enumerate(nums):
            if i == target:
                return pos
            elif i < target and nums[pos + 1] > target:
                return pos + 1


class TestPosistion(unittest.TestCase):

    def test_1356_5(self):
        input = search_input_pos([1, 3, 5, 6], 5)
        output = 2
        self.assertEqual(input, output)

    def test_1356_2(self):
        input = search_input_pos([1, 3, 5, 6], 2)
        output = 1
        self.assertEqual(input, output)

    def test_1356_7(self):
        input = search_input_pos([1, 3, 5, 6], 7)
        output = 4
        self.assertEqual(input, output)

    def test_1356_0(self):
        input = search_input_pos([1, 3, 5, 6], 0)
        output = 0
        self.assertEqual(input, output)

    def test_minus13560_1(self):
        input = search_input_pos([-6, -5, -3, -1, 0], 1)
        output = 5
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
