import unittest


# O(n) time, O(1) space solution
def buy_sell(prices: list) -> int:
    max_profit = 0
    p1, p2 = 0, 1
    while p2 < len(prices):
        if prices[p1] < prices[p2]:
            max_profit += prices[p2] - prices[p1]
        p1 += 1
        p2 += 1
    return max_profit


class TestMaxProfit(unittest.TestCase):
    def test_7(self):
        self.assertEqual(buy_sell([7, 1, 5, 3, 6, 4]), 7)

    def test_4(self):
        self.assertEqual(buy_sell([1, 2, 3, 4, 5]), 4)

    def test_0(self):
        self.assertEqual(buy_sell([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
