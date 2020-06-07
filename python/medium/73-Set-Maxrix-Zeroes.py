import unittest


# O(n*m) time, O(1) space solution
class Solution:
    def __init__(self):
        self._matrix = []
        self._locations = []

    def get_matrix(self):
        return self._matrix

    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self._matrix = matrix
        self.process_matrix()

    def process_matrix(self) -> None:
        self._find_zeroes()
        if self._locations:
            self._set_zeroes()

    def _find_zeroes(self):
        for row_index, row in enumerate(self._matrix):
            for col_index, col in enumerate(row):
                if col == 0:
                    self._locations.append((row_index, col_index))

    def _set_zeroes(self) -> None:
        for location in self._locations:
            self._spread_zeroes(location[0], location[1])

    def _spread_zeroes(self, row, col):
        self._spread_zeroes_left(row, col - 1)
        self._spread_zeroes_right(row, col + 1)
        self._spread_zeroes_down(row + 1, col)
        self._spread_zeroes_up(row - 1, col)

    def _inbounds(self, row, col):
        if row in range(len(self._matrix)) and col in range(len(self._matrix[0])):
            return True
        return False

    def _spread_zeroes_left(self, row, col):
        if not self._inbounds(row, col):
            return
        self._matrix[row][col] = 0
        self._spread_zeroes_left(row, col - 1)

    def _spread_zeroes_right(self, row, col):
        if not self._inbounds(row, col):
            return
        self._matrix[row][col] = 0
        self._spread_zeroes_right(row, col + 1)

    def _spread_zeroes_down(self, row, col):
        if not self._inbounds(row, col):
            return
        self._matrix[row][col] = 0
        self._spread_zeroes_down(row + 1, col)

    def _spread_zeroes_up(self, row, col):
        if not self._inbounds(row, col):
            return
        self._matrix[row][col] = 0
        self._spread_zeroes_up(row - 1, col)

class TestSetZeroes(unittest.TestCase):
    def test_non_square(self):
        matrix = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]
        solution = [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]
        solve = Solution()
        solve.setZeroes(matrix)
        self.assertEqual(solve.get_matrix(), solution)

    def test_middle_zero(self):
        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        solution = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        solve = Solution()
        solve.setZeroes(matrix)
        self.assertEqual(solve.get_matrix(), solution)

    def test_corner_zeroes(self):
        matrix = [
            [0, 1, 1],
            [1, 1, 1],
            [1, 1, 0]
        ]
        solution = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        solve = Solution()
        solve.setZeroes(matrix)
        self.assertEqual(solve.get_matrix(), solution)

    def test_all_zeroes(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        solution = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        solve = Solution()
        solve.setZeroes(matrix)
        self.assertEqual(solve.get_matrix(), solution)

    def test_no_zeroes(self):
        matrix = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        solution = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        solve = Solution()
        solve.setZeroes(matrix)
        self.assertEqual(solve.get_matrix(), solution)


if __name__ == "__main__":
    unittest.main()
