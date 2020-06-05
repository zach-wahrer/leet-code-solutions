import unittest


# O(n) time / O(1) space solution
def max_profit(prices: list) -> int:
    best_profit = 0
    for i in range(1, len(prices)):
        sale = prices[i] - prices[i - 1]
        best_profit = max(best_profit, best_profit + sale)
    return best_profit


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
