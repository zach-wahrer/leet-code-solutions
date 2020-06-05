import unittest


# Doesn't pass all leetcode tests
def max_square_incomplete(matrix: list) -> int:

    def _key_gen(row, col):
        if row not in range(len(matrix)) or col not in range(len(matrix[0])):
            return False
        key = (row, col)
        return key

    def _measure_col(row, col):
        square_col_size = 0
        while _key_gen(row, col) and matrix[row][col] == "1":
            square_col_size += 1
            col += 1
        return square_col_size

    def _measure_square(row, col):
        square_row_size = 0
        column_sizes = []
        while _key_gen(row, col) and matrix[row][col] == "1":
            column_sizes.append(_measure_col(row, col))
            square_row_size += 1
            row += 1
        return min(column_sizes + [square_row_size])

    square_dimensions = []

    for row_index, row_value in enumerate(matrix):
        for col_index, col_value in enumerate(row_value):
            if col_value == "1":
                square_dimensions.append(_measure_square(row_index, col_index))

    return max(square_dimensions) ** 2 if square_dimensions else 0


# O(n*m) time/space solution
def max_square(matrix: list) -> int:

    if not matrix:
        return 0

    dp = [[0 for char in row] for row in matrix]

    max_square_edge = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "1":
                dp[row][col] = 1 + min(dp[row][col-1], dp[row-1][col-1], dp[row-1][col])

            max_square_edge = max(max_square_edge, dp[row][col])

    return max_square_edge ** 2


class TestMaxSquare(unittest.TestCase):
    def test_4(self):
        grid = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
        self.assertEqual(max_square(grid), 4)
    #

    def test_1(self):
        grid = [["1"]]
        self.assertEqual(max_square(grid), 1)

    def test_9(self):
        grid = [
            ["0", "0", "1", "0"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "0"],
            ["1", "1", "0", "0"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "0"]
        ]
        self.assertEqual(max_square(grid), 9)


if __name__ == "__main__":
    unittest.main()
