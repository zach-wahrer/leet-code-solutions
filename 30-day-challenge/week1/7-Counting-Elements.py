import unittest


def count_elements(arr: list) -> int:
    pass


class TestCounts(unittest.TestCase):
    def test_short(self):
        self.assertEqual(count_elements([1, 2, 3]), 2)

    def test_long(self):
        self.assertEqual(count_elements([1, 1, 3, 3, 5, 5, 7, 7]), 0)

    def test_medium(self):
        self.assertEqual(count_elements([1, 3, 2, 3, 5, 0]), 3)

    def test_duplicates(self):
        self.assertEqual(count_elements([1, 1, 2, 2]), )
