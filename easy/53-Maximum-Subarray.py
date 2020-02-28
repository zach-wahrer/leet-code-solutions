import unittest


def max_subarray(nums: list) -> int:
    pass


class TestMaxSubarray(unittest.TestCase):

    def test_long_list_6(self):
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_1_1(self):
        self.assertEqual(max_subarray([1]), 1)

    def test_0000_0(self):
        self.assertEqual(max_subarray([0, 0, 0, 0]), 0)

    def test_12_3(self):
        self.assertEqual(max_subarray([1, 2]), 3)
