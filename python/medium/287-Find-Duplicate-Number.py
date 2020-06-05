import unittest


# Naive solution, O(n) space and time
# Iterate over list, checking against a set for what we've already seen
# Add to set if we haven't already seen it
def find_duplicate_num_naive(nums: list) -> int:
    if nums:
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)
    return None


# Tortise/hare solution, O(1) space, O(n) time
# Set two pointers to go through nums, one incrementing at i+1 and other i+2
# Check if they are equal, if so, return
# Check that pointer doesn't run off end of list
# Fails test_43142
def find_duplicate_num_tortise(nums: list) -> int:
    if nums:
        tortise, hare = 0, 1
        while True:
            if nums[tortise] == nums[hare]:
                return nums[hare]
            tortise += 1
            hare += 2
            if tortise > len(nums) - 1:
                tortise %= 2
            if hare > len(nums) - 1:
                hare = 0
    return None


# Count solution, O(n) space and time
def find_duplicate_num(nums: list) -> int:
    from collections import Counter
    if nums:
        counts = Counter(nums)
        for number, count in counts.items():
            if count > 1:
                return number
    return None


class TestForDuplicates(unittest.TestCase):

    def test_13422(self):
        input = find_duplicate_num([1, 3, 4, 2, 2])
        self.assertEqual(input, 2)

    def test_31342(self):
        input = find_duplicate_num([3, 1, 3, 4, 2])
        self.assertEqual(input, 3)

    def test_1231(self):
        input = find_duplicate_num([1, 2, 3, 1])
        self.assertEqual(input, 1)

    def test_blank(self):
        input = find_duplicate_num([])
        self.assertEqual(input, None)

    def test_two(self):
        input = find_duplicate_num([1, 1])
        self.assertEqual(input, 1)

    def test_three(self):
        input = find_duplicate_num([1, 2, 2])
        self.assertEqual(input, 2)

    def test_43142(self):
        input = find_duplicate_num([4, 3, 1, 4, 2])
        self.assertEqual(input, 4)


if __name__ == "__main__":
    unittest.main()
