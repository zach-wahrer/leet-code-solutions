import unittest


def max_square(matrix: list) -> int:
    pass


class TestMaxSquare(unittest.TestCase):
    def test_4(self):
        grid = [
            ["1 0 1 0 0"],
            ["1 0 1 1 1"],
            ["1 1 1 1 1"],
            ["1 0 0 1 0"]
        ]
        self.assertEqual(max_square(grid), 4)
