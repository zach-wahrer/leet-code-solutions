import unittest


# Iterative O(n) time, O(1) space solution
def max_subarray(nums: list) -> int:
    tmp_sum = nums[0]
    max_sum = nums[0]

    for i in nums[1:]:
        tmp_sum = (max(tmp_sum + i, i))
        if tmp_sum > max_sum:
            max_sum = tmp_sum

    return max_sum


class TestMaxSubarray(unittest.TestCase):
    def test_long(self):
        sub = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(sub, 6)

    def test_short(self):
        sub = max_subarray([-2, 1])
        self.assertEqual(sub, 1)

    def test_one(self):
        sub = max_subarray([-2])
        self.assertEqual(sub, -2)


if __name__ == "__main__":
    unittest.main()
