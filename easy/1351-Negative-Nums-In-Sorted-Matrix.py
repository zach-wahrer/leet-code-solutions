import unittest


# Naive O(n + m) time, O(1) space
def count_negatives_simple(grid: list) -> int:
    counter = 0
    for row in grid:
        for number in row:
            if number < 0:
                counter += 1
    return counter


# Binary seach O(log(n) * m) time, O(1) space
def count_negatives(grid: list) -> int:
    counter = 0

    if not grid[0]:
        return counter

    on_row = 0

    while on_row < len(grid):
        left = 0
        right = len(grid[0]) - 1
        whole_row = False
        first_negative = None

        if grid[on_row][right] >= 0:
            on_row += 1
            continue
        if grid[on_row][left] < 0:
            first_negative = 0
            whole_row = True

        while left <= right and whole_row is False:
            middle = (right + left) // 2
            if grid[on_row][middle] < 0 and grid[on_row][middle - 1] >= 0:
                first_negative = middle
                break

            if grid[on_row][middle] >= 0:
                left = middle + 1
            else:
                right = middle - 1

        if first_negative >= 0:
            counter += len(grid[on_row]) - first_negative

        on_row += 1

    return counter


class TestNegativesInMaxtrix(unittest.TestCase):

    def test_8(self):
        input = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        self.assertEqual(count_negatives(input), 8)

    def test_0(self):
        input = [[3, 2], [1, 0]]
        self.assertEqual(count_negatives(input), 0)

    def test_3(self):
        input = [[1, -1], [-1, -1]]
        self.assertEqual(count_negatives(input), 3)

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
