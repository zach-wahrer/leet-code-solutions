import unittest


# Dynamic recursive solution
def find_perimeter(grid: list) -> int:

    def _key_gen(row, col):
        if row in range(len(grid)) and col in range(len(grid[0])):
            return (row, col)
        return 'oob'

    memoize = {'oob': float('-inf')}

    def _find_land(row, col):
        key = _key_gen(row, col)

        if key not in memoize:
            if grid[row][col] == 1:
                return row, col
            else:
                memoize[key] = -1
            right = _find_land(row, col + 1)
            down = _find_land(row + 1, col)
            return right if right else down

    def _spread_count(row, col):
        key = _key_gen(row, col)

        if key not in memoize and grid[row][col] == 1:
            memoize[key] = 4

            down = _spread_count(row + 1, col)
            right = _spread_count(row, col + 1)
            up = _spread_count(row - 1, col)
            left = _spread_count(row, col - 1)

            perimeter_value = 4
            for direction in [down, right, up, left]:
                if direction:
                    perimeter_value -= 1

            memoize[key] = perimeter_value
            return True

        if key not in memoize:
            memoize[key] = -1
            return False

        if memoize[key] >= 0:
            return True

        return False

    first_land = _find_land(0, 0)

    if first_land:
        _spread_count(first_land[0], first_land[1])

    parimeter = 0
    for value in memoize.values():
        if value != float('-inf') and value != -1:
            parimeter += value

    return parimeter


class TestPerimeter(unittest.TestCase):

    def test_leet_12_2(self):
        grid = [[1, 1, 0],
                [1, 1, 1],
                [1, 1, 0]]
        self.assertEqual(find_perimeter(grid), 12)

    def test_leet_12(self):
        grid = [[0, 1, 0],
                [1, 1, 1],
                [1, 1, 0]]
        self.assertEqual(find_perimeter(grid), 12)

    def test_basic_4(self):
        grid = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        self.assertEqual(find_perimeter(grid), 4)

    def test_basic_6(self):
        grid = [[1],
                [1],
                [0]]
        self.assertEqual(find_perimeter(grid), 6)

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
