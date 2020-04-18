import unittest


# Exceeds time on leetcode
def minimum_path(grid: list) -> int:

    def _key_gen(row, col):
        if row not in range(len(grid)) or col not in range(len(grid[0])):
            return "oob"
        return (row, col)

    def _traverse(row, col):
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return grid[row][col]

        key = _key_gen(row, col)

        if key == "oob":
            return float('inf')

        min_path = min(_traverse(row + 1, col), _traverse(row, col + 1))
        return grid[row][col] + min_path

    return _traverse(0, 0)


class TestMinPath(unittest.TestCase):
    def test_7(self):
        map = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        self.assertEqual(minimum_path(map), 7)

    def test_5(self):
        map = [
            [1, 1, 1],
            [1, 5, 1],
            [1, 2, 1]
        ]
        self.assertEqual(minimum_path(map), 5)

    def test_3(self):
        map = [
            [1, 0, 1],
            [1, 5, 0],
            [1, 2, 1]
        ]
        self.assertEqual(minimum_path(map), 3)


if __name__ == "__main__":
    unittest.main()
