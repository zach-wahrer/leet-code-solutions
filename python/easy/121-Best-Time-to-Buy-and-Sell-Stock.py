import unittest


# Naive - Times out on leetcode
def max_profit_naive(prices: list) -> int:
    max_profit = 0
    for index, buy_price in enumerate(prices):
        for sell_price in prices[index + 1:]:
            max_profit = max((sell_price - buy_price), max_profit)

    return max_profit

# Doesn't pass all tests


def max_profit_non_functional(prices: list) -> int:
    max_price = max(prices)
    min_price = min(prices)
    max_index = prices.index(max_price)
    min_index = prices.index(min_price)

    while max_index < min_index:
        print(max_index, min_index)
        prices.pop(max_index)
        max_price = max(prices)
        max_index = prices.index(max_price)
        if len(prices) == 1:
            return 0

    return max(max_price - min_price, 0)


# O(n) time, O(1) space solution
def max_profit(prices: list) -> int:
    max_seen = -1
    min_seen = -1
    max_profit = 0

    for i in prices:
        if i > max_seen and min_seen != -1:
            max_seen = i
            max_profit = max(max_profit, max_seen - min_seen)

        if i < min_seen or min_seen == -1:
            min_seen = i
            max_seen = -1

    return max_profit


class TestMaxProfit(unittest.TestCase):

    def test_2121012_2(self):
        self.assertEqual(max_profit([2, 1, 2, 1, 0, 1, 2]), 2)

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
