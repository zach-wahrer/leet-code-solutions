import unittest


def min_set_to_half(arr: list) -> int:
    pass


class TestMinimumSet(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
