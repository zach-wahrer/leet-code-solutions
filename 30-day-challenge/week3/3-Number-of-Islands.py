import unittest


def num_of_islands(grid: list) -> int:
    pass


class TestIslands(unittest.TestCase):
    def test_1_island(self):
        map = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(num_of_islands(map), 1)

    def test_3_islands(self):
        map = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        self.assertEqual(num_of_islands(map), 3)


if __name__ == "__main__":
    unittest.main()
