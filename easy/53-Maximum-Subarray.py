import unittest


# O(n) time and O(1) space solution
def max_subarray(nums: list) -> int:
    max_ending_here = 0
    max_so_far = 0

    for i in nums:
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far


class TestMaxSubarray(unittest.TestCase):

    def test_long_list_6(self):
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_1_1(self):
        self.assertEqual(max_subarray([1]), 1)

    def test_0000_0(self):
        self.assertEqual(max_subarray([0, 0, 0, 0]), 0)

    def test_12_3(self):
        self.assertEqual(max_subarray([1, 2]), 3)


if __name__ == "__main__":
    unittest.main()
