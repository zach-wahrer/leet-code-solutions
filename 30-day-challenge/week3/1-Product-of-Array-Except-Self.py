import unittest


def product_except_self(nums: list) -> list:
    pass


class TestProducts(unittest.TestCase):
    def test_1234(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_12(self):
        self.assertEqual(product_except_self([1, 2]), [2, 1])
