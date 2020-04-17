import unittest


# O(n*m) solution
def num_of_islands(grid: list) -> int:

    def _key_gen(row, col, memoize, grid):
        key = (row, col)
        if key in memoize or row not in range(len(grid)) or col not in range(len(grid[0])):
            return False
        memoize.add(key)
        return key

    def _spread(key, memoize, grid):
        if not key:
            return

        row, col = key

        if grid[row][col] != 0:
            right = _key_gen(row, col + 1, memoize, grid)
            left = _key_gen(row, col - 1, memoize, grid)
            up = _key_gen(row - 1, col, memoize, grid)
            down = _key_gen(row + 1, col, memoize, grid)

            _spread(right, memoize, grid)
            _spread(left, memoize, grid)
            _spread(up, memoize, grid)
            _spread(down, memoize, grid)

    memoize = set()
    count = 0

    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            key = _key_gen(row_index, col_index, memoize, grid)
            if key and col == 1:
                count += 1
                _spread(key, memoize, grid)

    return count


class TestIslands(unittest.TestCase):
    def test_1_island(self):
        map = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(num_of_islands(map), 1)

    def test_3_islands(self):
        map = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        self.assertEqual(num_of_islands(map), 3)


if __name__ == "__main__":
    unittest.main()
