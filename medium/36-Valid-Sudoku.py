import unittest


# O(n) solution
def is_valid_sudoku(board: list) -> bool:
    def is_metric_valid(values):
        uniques = set()
        for i in values:
            if i != "." and i not in uniques:
                uniques.add(i)
            elif i in uniques:
                return False
        return True

    for row in board:
        if not is_metric_valid(row):
            return False

    col_ptr = 0
    while col_ptr < len(board[0]):
        col = [board[0][col_ptr], board[1][col_ptr], board[2][col_ptr],
               board[3][col_ptr], board[4][col_ptr], board[5][col_ptr],
               board[6][col_ptr], board[7][col_ptr], board[8][col_ptr]]
        if not is_metric_valid(col):
            return False
        col_ptr += 1

    sub_grids = [[], [], [], [], [], [], [], [], []]
    for index, row in enumerate(board):
        if index in range(3):
            sub_grids[0] += row[:3]
            sub_grids[1] += row[3:6]
            sub_grids[2] += row[6:]
        elif index in range(3, 6):
            sub_grids[3] += row[:3]
            sub_grids[4] += row[3:6]
            sub_grids[5] += row[6:]
        else:
            sub_grids[6] += row[:3]
            sub_grids[7] += row[3:6]
            sub_grids[8] += row[6:]

    for sub_grid in sub_grids:
        if not is_metric_valid(sub_grid):
            return False

    return True


class TestValidSudoku(unittest.TestCase):
    def test_valid(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.assertTrue(is_valid_sudoku(board))

    def test_invalid(self):
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.assertFalse(is_valid_sudoku(board))

    def test_invalid_row(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "7"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.assertFalse(is_valid_sudoku(board))

    def test_invalid_col(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "9"],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "7"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.assertFalse(is_valid_sudoku(board))

    def test_invalid_subgrid(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "9"],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "7"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", "5", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.assertFalse(is_valid_sudoku(board))


if __name__ == "__main__":
    unittest.main()
