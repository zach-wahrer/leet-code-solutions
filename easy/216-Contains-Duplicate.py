import unittest


def contains_duplicate(nums: list) -> bool:
    pass


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
