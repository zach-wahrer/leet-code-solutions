import unittest


def product_array_except_self(nums: list) -> list:
    pass


class TestProductArray(unittest.TestCase):
    def test_1234(self):
        input = product_array_except_self([1, 2, 3, 4])
        self.assertEqual(input, [24, 12, 8, 6])

    def test_12(self):
        input = product_array_except_self([1, 2])
        self.assertEqual(input, [2, 1])

    def test_012(self):
        input = product_array_except_self([0, 1, 2])
        self.assertEqual(input, [2, 0, 0])

    def test_012(self):
        input = product_array_except_self([1, 2, 3])
        self.assertEqual(input, [6, 3, 2])


if __name__ == "__main__":
    unittest.main()
