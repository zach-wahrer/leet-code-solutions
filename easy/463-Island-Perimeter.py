import unittest


def find_perimeter(grid: list) -> int:
    pass


class TestPerimeter(unittest.TestCase):

    def test_basic_4(self):
        grid = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        self.assertEqual(find_perimeter(grid), 12)

    def test_simple_12(self):
        grid = [[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]]
        self.assertEqual(find_perimeter(grid), 12)

    def test_moderate_16(self):
        grid = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0]]
        self.assertEqual(find_perimeter(grid), 16)

    def test_unconventional_22(self):
        grid = [[0, 1, 0, 0, 1],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0]]
        self.assertEqual(find_perimeter(grid), 22)


if __name__ == "__main__":
    unittest.main()
