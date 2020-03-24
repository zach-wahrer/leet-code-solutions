import unittest


# O(n) time/space solution
def find_majority(nums: list) -> int:
    from collections import Counter

    counts = Counter(nums)

    majority = [0, float('-inf')]
    for i in counts:
        if counts[i] > majority[1]:
            majority[0] = i
            majority[1] = counts[i]

    return majority[0]


class TestFindMajority(unittest.TestCase):

    def test_323(self):
        self.assertEqual(find_majority([3, 2, 3]), 3)

    def test_2211122(self):
        self.assertEqual(find_majority([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
