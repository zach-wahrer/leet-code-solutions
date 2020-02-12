import unittest


# Naive solution, O(n) space and time
# Loop through the nums, checking if we've seen them before
# If so, output to a list of duplicates
def find_all_duplicates_set(nums: list) -> list:
    seen = set()
    dupes = []
    for i in nums:
        if i in seen and i not in dupes:
            dupes.append(i)
        else:
            seen.add(i)
    return dupes


# Two pointer solution, O(n(logn)) time, O(1) space
# Exceeds time limit on leet code
def find_all_duplicates(nums: list) -> list:
    left = 0
    right = 1
    dupes = []
    while left < len(nums):
        while right < len(nums):
            if nums[left] == nums[right]:
                dupes.append(nums[left])
            right += 1
        left += 1
        right = left + 1
    return dupes


class TestAllDuplicates(unittest.TestCase):

    def test_43278231(self):
        input = find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1])
        self.assertEqual(input, [2, 3])

    def test_22222(self):
        input = find_all_duplicates([2, 2, 2, 2, 2])
        self.assertEqual(input, [2])

    def test_empty(self):
        input = find_all_duplicates([])
        self.assertEqual(input, [])

    def test_two(self):
        input = find_all_duplicates([1, 1])
        self.assertEqual(input, [1])

    def test_three(self):
        input = find_all_duplicates([1, 1, 2])
        self.assertEqual(input, [1])

    def test_98765511(self):
        input = find_all_duplicates([9, 8, 7, 8, 5, 5, 1, 1])
        self.assertEqual(input, [8, 5, 1])


if __name__ == "__main__":
    unittest.main()
