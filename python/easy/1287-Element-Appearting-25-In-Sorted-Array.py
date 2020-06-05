import unittest


# Naive O(n) time and space
def find_25_int(arr: list) -> int:
    from collections import Counter

    counts = Counter(arr)
    greatest_seen = 0
    most_frequent_number = None

    for i in counts:
        if counts[i] > greatest_seen:
            greatest_seen = counts[i]
            most_frequent_number = i

    return most_frequent_number


class TestFind25(unittest.TestCase):

    def test_6(self):
        self.assertEqual(find_25_int([1, 2, 2, 6, 6, 6, 6, 7, 10]), 6)

    def test_one_item(self):
        self.assertEqual(find_25_int([0]), 0)

    def test_8(self):
        self.assertEqual(find_25_int([8, 8, 8, 8, 8]), 8)

    def test_2(self):
        self.assertEqual(find_25_int([1, 2, 2, 3, 4, 5, 6]), 2)


if __name__ == '__main__':
    unittest.main()
