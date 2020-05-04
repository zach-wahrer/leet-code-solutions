import unittest


def max_profit(prices: list) -> int:
    pass


class TestMaxProfit(unittest.TestCase):
    def test_715364(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 7)

    def test_12345(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)

    def test_76431(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)


if __name__ == "__main__":
    unittest.main()
