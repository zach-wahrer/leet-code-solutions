import unittest


# Naive
def max_profit(prices: list) -> int:
    profits = [0]
    for index, buy_price in enumerate(prices):
        for sell_price in prices[index + 1:]:
            profits.append(sell_price - buy_price)

    return max(profits)


class TestMaxProfit(unittest.TestCase):

    def test_715364_5(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)

    def test_765431_0(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)

    def test_12_1(self):
        self.assertEqual(max_profit([1, 2]), 1)

    def test_blank_0(self):
        self.assertEqual(max_profit([]), 0)

    def test_1_0(self):
        self.assertEqual(max_profit([1]), 0)

    def test_1234560_5(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 0]), 5)


if __name__ == "__main__":
    unittest.main()
