import unittest


# Naive O(n) solution
def find_min(nums: list) -> int:
    try:
        return min(nums)
    except ValueError:
        return None


class TestMinimumRotatedSortedArray(unittest.TestCase):

    def test_34512(self):
        input = find_min([3, 4, 5, 1, 2])
        self.assertEqual(input, 1)

    def test_4567012(self):
        input = find_min([4, 5, 6, 7, 0, 1, 2])
        self.assertEqual(input, 0)

    def test_99100567(self):
        input = find_min([99, 100, 5, 6, 7])
        self.assertEqual(input, 5)

    def test_blank(self):
        input = find_min([])
        self.assertEqual(input, None)

    def test_two_items(self):
        input = find_min([2, 1])
        self.assertEqual(input, 1)

    def test_one_item(self):
        input = find_min([100])
        self.assertEqual(input, 100)

    def test_three_items(self):
        input = find_min([100, 101, 99])
        self.assertEqual(input, 99)


if __name__ == "__main__":
    unittest.main()
