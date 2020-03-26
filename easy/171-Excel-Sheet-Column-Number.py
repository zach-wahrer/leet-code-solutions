import unittest


# O(n) time, O(1) space solution
def column_number(s: str) -> int:
    values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
              'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
              'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
              'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    output = 0
    place = 1

    for i in s[::-1]:
        output += place * values[i]
        place *= 26

    return output


class TestColumnNumber(unittest.TestCase):

    def test_A(self):
        self.assertEqual(column_number('A'), 1)

    def test_C(self):
        self.assertEqual(column_number('C'), 3)

    def test_AA(self):
        self.assertEqual(column_number('AA'), 27)

    def test_AB(self):
        self.assertEqual(column_number('AB'), 28)

    def test_BA(self):
        self.assertEqual(column_number('BA'), 53)

    def test_ZY(self):
        self.assertEqual(column_number('ZY'), 701)


if __name__ == "__main__":
    unittest.main()
