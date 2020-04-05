import unittest


def buy_sell(prices: list) -> int:
    pass


class TestMaxProfit(unittest.TestCase):
    def test_7(self):
        self.assertEqual(buy_sell([7, 1, 5, 3, 6, 4]), 7)

    def test_4(self):
        self.assertEqual(buy_sell([1, 2, 3, 4, 5]), 4)

    def test_0(self):
        self.assertEqual(buy_sell([7, 6, 4, 3, 1]), 0)
