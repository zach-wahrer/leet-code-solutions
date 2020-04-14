import unittest


def shift_string(s: str, shift: list) -> str:
    pass


class TestStringShift(unittest.TestCase):
    def test_abc(self):
        self.assertEqual(shift_string('abc', [[0, 1], [1, 2]]), 'cab')

    def test_abcdefg(self):
        self.assertEqual(shift_string('abc',
                                      [[1, 1], [1, 1], [0, 2], [1, 3]]), 'efgabcd')


if __name__ == "__main__":
    unittest.main()
