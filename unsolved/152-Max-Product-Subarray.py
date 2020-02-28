import unittest


# Doesn't pass all tests
def max_product(nums: list) -> int:
    tmp_max = nums[0]
    max_so_far = nums[0]

    for i in nums[1:]:
        tmp_max = max(tmp_max * i, i)
        if tmp_max > max_so_far:
            max_so_far = tmp_max

    return max_so_far


class TestMaxProduct(unittest.TestCase):

    def test_2324_6(self):
        self.assertEqual(max_product([2, 3, -2, 4]), 6)

    def test_201_0(self):
        self.assertEqual(max_product([-2, 0, -1]), 0)

    def test_1_0(self):
        self.assertEqual(max_product([1]), 1)

    def test_10_0(self):
        self.assertEqual(max_product([1, 0]), 1)

    def test_3103_3(self):
        self.assertEqual(max_product([3, 1, 0, 3]), 3)

    def test_2316_6(self):
        self.assertEqual(max_product([-2, -3, 1, 6]), 36)

    def test_203_0(self):
        self.assertEqual(max_product([-2, 0, -3]), 0)

    def test_230_0(self):
        self.assertEqual(max_product([-2, -3, 0]), 6)

    def test_234_24(self):
        self.assertEqual(max_product([-2, 3, -4]), 24)


if __name__ == "__main__":
    unittest.main()
