import unittest


def max_product(nums: list) -> int:
    pass


class TestMaxProduct(unittest.TestCase):

    def test_2324_6(self):
        self.assertEqual(max_product([2, 3, -2, 4]), 6)

    def test_201_0(self):
        self.assertEqual(max_product([-2, 0, -1]), 0)

    def test_1_0(self):
        self.assertEqual(max_product[1], 0)

    def test_10_0(self):
        self.assertEqual(max_product[1, 0], 0)

    def test_3103_3(self):
        self.assertEqual(max_product[3, 1, 0, 3], 3)

    def test_2316_6(self):
        self.assertEqual(max_product[-2, -3, 1, 6], 0)

    def test_23_2(self):
        self.assertEqual(max_product[-2, -3], -2)

    def test_230_0(self):
        self.assertEqual(max_product[-2, -3, 0], 0)
