import unittest


def max_subarray(nums: list) -> int:
    pass


class TestMaxSubarray(unittest.TestCase):
    def test_long(self):
        sub = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(sub, 6)
