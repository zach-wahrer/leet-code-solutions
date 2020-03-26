import unittest


def column_number(s: str) -> int:
    pass


class TestColumnNumber(unittest.TestCase):

    def test_A(self):
        self.assertEqual(column_number('A'), 1)

    def test_C(self):
        self.assertEqual(column_number('C'), 3)

    def test_AA(self):
        self.assertEqual(column_number('AA'), 27)

    def test_AB(self):
        self.assertEqual(column_number('AB'), 28)

    def test_ZY(self):
        self.assertEqual(column_number('ZY'), 701)


if __name__ == "__main__":
    unittest.main()
