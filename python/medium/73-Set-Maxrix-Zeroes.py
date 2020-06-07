import unittest

def process_matrix(maxrix: list) -> None:
    pass

def find_zeroes(matrix: list) -> list:
    pass

def set_zeroes(locations: list) -> None:
    pass


class TestSetZeroes(unittest.TestCase):
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
        self.assertEqual(process_matrix(matrix), solution)

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
        self.assertEqual(process_matrix(matrix), solution)

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
        self.assertEqual(process_matrix(matrix), solution)

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
        self.assertEqual(process_matrix(matrix), solution)
