import unittest


# Naive O(n**2) time solution
def contains_duplicate_naive(nums: list) -> bool:
    for index, value in enumerate(nums):
        if value in nums[index + 1:]:
            return True
    return False


def contains_duplicate(nums: list) -> bool:
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False


class TestContainsDuplicate(unittest.TestCase):

    def test_1231_true(self):
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))

    def test_1234_false(self):
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))

    def test_multi_true(self):
        self.assertTrue(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_blank_false(self):
        self.assertFalse(contains_duplicate([]))

    def test_1_false(self):
        self.assertFalse(contains_duplicate([1]))

    def test_12_false(self):
        self.assertFalse(contains_duplicate([1, 2]))

    def test_22_true(self):
        self.assertTrue(contains_duplicate([2, 2]))


if __name__ == "__main__":
    unittest.main()
