import unittest


def count_negatives(grid: list) -> int:
    pass


class TestNegativesInMaxtrix(unittest.TestCase):

    def test_8(self):
        input = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        self.assertEqual(count_negatives(input), 8)

    def test_0(self):
        input = [[3, 2], [1, 0]]
        self.assertEqual(count_negatives(input), 0)

    def test_3(self):
        input = [[1, -1], [-1, -1]]
        self.assertEqual(count_negatives(input), 8)

    def test_1(self):
        input = [[-1]]
        self.assertEqual(count_negatives(input), 1)

    def test_blank(self):
        input = [[]]
        self.assertEqual(count_negatives(input), 0)

    def test_uneven(self):
        input = [[4, 3, 1, 1], [4, 3, -1, -1, -2], [4, 3, 1, 1]]
        self.assertEqual(count_negatives(input), 3)


if __name__ == "__main__":
    unittest.main()
