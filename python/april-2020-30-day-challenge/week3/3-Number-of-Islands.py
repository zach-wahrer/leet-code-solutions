import unittest


# O(n*m) solution
def num_of_islands(grid: list) -> int:

    def _key_gen(row, col):
        key = (row, col)
        if key in memoize or row not in range(len(grid)) or col not in range(len(grid[0])):
            return False
        memoize.add(key)
        return key

    def _spread(key):
        if not key:
            return

        row, col = key

        if grid[row][col] != 0:
            _spread(_key_gen(row, col + 1))
            _spread(_key_gen(row, col - 1))
            _spread(_key_gen(row - 1, col))
            _spread(_key_gen(row + 1, col))

    memoize = set()
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            key = _key_gen(row, col)
            if key and grid[row][col] == 1:
                count += 1
                _spread(key)

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
