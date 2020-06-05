import unittest


# O(n) time and O(1) space solution - Only works if there is a 1 in the list.
# Sort nums
# If nums[0] > 1, return 1
# If
def find_first_missing_positive_non_func(nums: list) -> int:
    nums.sort()

    if not nums or nums[0] > 1:  # Blank or all positive edge case
        return 1

    pointer = 0
    while pointer < len(nums) - 1:
        if nums[pointer] + 1 != nums[pointer + 1] and nums[pointer] > 0:
            return nums[pointer] + 1
        pointer += 1

    if nums[pointer] < 1:  # All negitive nums edge case
        return 1

    return nums[pointer] + 1


# Getting too complicated and messy. Need to learn more.
def find_first_missing_positive(nums: list) -> int:
    nums.sort()

    if not nums or nums[0] > 1:  # Blank or all positive edge case
        return 1

    pointer = 0
    while pointer < len(nums) - 1:
        if nums[pointer] + 1 != nums[pointer + 1] and nums[pointer] > 0:
            return nums[pointer] + 1
        pointer += 1

    if nums[pointer] < 1:  # All negitive nums edge case
        return 1

    if nums[pointer] == nums[pointer - 1] + 1:  # List in order edge case
        return nums[pointer] + 1

    if nums[pointer] == 1:
        return 2

    return nums[pointer] - (nums[pointer] - 1)


class TestFirstMissingPos(unittest.TestCase):

    def test_02211(self):
        input = find_first_missing_positive([0, 2, 2, 1, 1])
        self.assertEqual(input, 3)

    def test_1(self):
        input = find_first_missing_positive([1])
        self.assertEqual(input, 2)

    def test_10001(self):
        input = find_first_missing_positive([1000, -1])
        self.assertEqual(input, 1)

    def test_120(self):
        input = find_first_missing_positive([1, 2, 0])
        self.assertEqual(input, 3)

    def test_3411(self):
        input = find_first_missing_positive([3, 4, -1, 1])
        self.assertEqual(input, 2)

    def test_7891112(self):
        input = find_first_missing_positive([7, 8, 9, 11, 12])
        self.assertEqual(input, 1)

    def test_blank(self):
        input = find_first_missing_positive([])
        self.assertEqual(input, 1)

    def test_4(self):
        input = find_first_missing_positive([-4])
        self.assertEqual(input, 1)

    def test_2(self):
        input = find_first_missing_positive([2])
        self.assertEqual(input, 1)


if __name__ == "__main__":
    unittest.main()
