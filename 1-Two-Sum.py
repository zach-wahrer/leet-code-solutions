'''
Psudocode:
    Loop through numbers
        Add current number to next number, seeing if match
        If no match found with that number, go to next
        Repeat
'''

import unittest


# Hash Algorithm
def check_sums(nums: list, target: int) -> list:
    number_hash = dict()
    for location, number in enumerate(nums):
        if target - number not in number_hash:
            number_hash[number] = location
        else:
            return [number_hash[target - number], location]


# List Algorithm
def check_sums_list(nums: list, target: int) -> list:
    for cur_position in range(len(nums)):
        for rem_numbers in range(cur_position + 1, len(nums)):
            if nums[cur_position] + nums[rem_numbers] == target:
                return [cur_position, rem_numbers]


class TestCheckSums(unittest.TestCase):

    def test_271115_9(self):
        input = check_sums([2, 7, 11, 15], 9)
        output = [0, 1]
        self.assertEqual(input, output)

    def test_1491312_17(self):
        input = check_sums([1, 4, 9, 13, 12], 17)
        output = [1, 3]
        self.assertEqual(input, output)

    def test_081616_32(self):
        input = check_sums([0, 8, 16, 16], 32)
        output = [2, 3]
        self.assertEqual(input, output)

    def test_101112_1(self):
        input = check_sums([10, -11, 12], -1)
        output = [0, 1]
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
