import unittest


# Dynamic O(n*m) solution
def minimum_path(grid: list) -> int:

    fin_row = len(grid) - 1
    fin_col = len(grid[0]) - 1
    memoize = {"oob": float('inf'), (fin_row, fin_col): grid[fin_row][fin_col]}

    def _key_gen(row, col):
        if row not in range(len(grid)) or col not in range(len(grid[0])):
            return "oob"
        return (row, col)

    def _traverse(row, col):
        key = _key_gen(row, col)

        if key not in memoize:
            min_path = min(_traverse(row + 1, col), _traverse(row, col + 1))
            memoize[key] = min_path + grid[row][col]

        return memoize[key]

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
