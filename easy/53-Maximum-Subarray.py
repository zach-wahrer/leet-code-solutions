import unittest


# O(n) time and O(1) space solution
def max_subarray(nums: list) -> int:

    tmp_sum = nums[0]
    max_sum = nums[0]

    for i in nums[1:]:
        tmp_sum = max(tmp_sum + i, i)
        if tmp_sum > max_sum:
            max_sum = tmp_sum

    return max_sum


class TestMaxSubarray(unittest.TestCase):

    def test_long_list_6(self):
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_1_1(self):
        self.assertEqual(max_subarray([1]), 1)

    def test_0000_0(self):
        self.assertEqual(max_subarray([0, 0, 0, 0]), 0)

    def test_12_3(self):
        self.assertEqual(max_subarray([1, 2]), 3)

    def test_minus_1(self):
        self.assertEqual(max_subarray([-1]), -1)

    def test_minus_test2_1(self):
        self.assertEqual(max_subarray([-2, -1]), -1)


if __name__ == "__main__":
    unittest.main()
