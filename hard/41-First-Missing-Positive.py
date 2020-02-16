import unittest


def find_first_missing_positive(nums: list) -> int:
    pass


class TestFirstMissingPos(unittest.TestCase):
    def test_120(self):
        input = find_first_missing_positive([1, 2, 0])
        self.assertEqual(input, 3)

    def test_3411(self):
        input = find_first_missing_positive([3, 4, -1, 1])
        self.assertEqual(input, 2)

    def test_7891112(self):
        input = find_first_missing_positive([7, 8, 9, 11, 12])
        self.assertEqual(input, 1)


if __name__ == "__main__":
    unittest.main()
