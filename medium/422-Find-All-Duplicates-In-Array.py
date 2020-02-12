import unittest


def find_all_duplicates(nums: list) -> list:
    pass


class TestAllDuplicates(unittest.TestCase):

    def test_43278231(self):
        input = find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1])
        self.assertEqual(input, [2, 3])

    def test_22222(self):
        input = find_all_duplicates([2, 2, 2, 2, 2])
        self.assertEqual(input, [2])

    def test_empty(self):
        input = find_all_duplicates([])
        self.assertEqual(input, [])

    def test_two(self):
        input = find_all_duplicates([1, 1])
        self.assertEqual(input, [1])

    def test_three(self):
        input = find_all_duplicates([1, 1, 2])
        self.assertEqual(input, [1])

    def test_98765511(self):
        input = find_all_duplicates([9, 8, 7, 8, 5, 5, 1, 1])
        self.assertEqual(input, [5, 1])


if __name__ == "__main__":
    unittest.main()
