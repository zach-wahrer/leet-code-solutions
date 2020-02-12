import unittest


def find_duplicate_num(sums: list) -> int:
    pass


class TestForDuplicates(unittest.TestCase):

    def test_13422(self):
        input = find_duplicate_num([1, 3, 4, 2, 2])
        self.assertEqual(input, 2)

    def test_31342(self):
        input = find_duplicate_num([3, 1, 3, 4, 2])
        self.assertEqual(input, 3)

    def test_1231(self):
        input = find_duplicate_num([1, 2, 3, 1])
        self.assertEqual(input, 1)

    def test_blank(self):
        input = find_duplicate_num([])
        self.assertEqual(input, None)

    def test_two(self):
        input = find_duplicate_num([1, 1])
        self.assertEqual(input, 1)

    def test_three(self):
        input = find_duplicate_num([1, 2, 2])
        self.assertEqual(input, 2)


if __name__ == "__main__":
    unittest.main()
