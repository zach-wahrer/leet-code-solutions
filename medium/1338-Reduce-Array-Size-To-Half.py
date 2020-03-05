import unittest
from collections import Counter


# O(n log n) time, O(n) space solution
def min_set_to_half(arr: list) -> int:
    counts_dict = Counter(arr)
    counts = [i for i in counts_dict.values()]
    counts.sort(reverse=True)
    acc = 0
    num_elements = 0
    for i in counts:
        acc += i
        num_elements += 1
        if acc >= len(arr) / 2:
            return num_elements
    return 0


class TestMinimumSet(unittest.TestCase):

    def test_longer_5(self):
        input = [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]
        self.assertEqual(min_set_to_half(input), 5)

    def test_long_2(self):
        input = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
        self.assertEqual(min_set_to_half(input), 2)

    def test_single(self):
        input = [7, 7, 7, 7, 7, 7]
        self.assertEqual(min_set_to_half(input), 1)

    def test_short(self):
        input = [1, 9]
        self.assertEqual(min_set_to_half(input), 1)

    def test_double(self):
        input = [1000, 1000, 3, 7]
        self.assertEqual(min_set_to_half(input), 1)

    def test_singles(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(min_set_to_half(input), 5)

    def test_blank(self):
        input = []
        self.assertEqual(min_set_to_half(input), 0)


if __name__ == "__main__":
    unittest.main()
