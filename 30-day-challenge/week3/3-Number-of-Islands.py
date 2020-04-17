import unittest


def num_of_islands(grid: list) -> int:

    def _key_gen(row, col, memoize, grid):
        if row not in range(len(grid)) or col not in range(len(grid[0])):
            return "oob"

        key = (row, col)
        if key in memoize:
            return "seen"
        memoize.add(key)
        return key

    def _spread(key, memoize, grid):
        if key == "seen" or key == "oob":
            return
        row, col = key
        if grid[row][col] == 0:
            return
        right = _key_gen(row, col + 1, memoize, grid)
        left = _key_gen(row, col - 1, memoize, grid)
        up = _key_gen(row - 1, col, memoize, grid)
        down = _key_gen(row + 1, col, memoize, grid)

        if right != 'seen' or 'oob':
            _spread(right, memoize, grid)
        if left != 'seen' or 'oob':
            _spread(left, memoize, grid)
        if up != 'seen' or 'oob':
            _spread(up, memoize, grid)
        if down != 'seen' or 'oob':
            _spread(down, memoize, grid)

    memoize = set()
    count = 0

    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            key = _key_gen(row_index, col_index, memoize, grid)
            if key != 'seen' and col == 1:
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
