import unittest


def binary_search(nums: list, target: int) -> int:
    pass


class TestBinarySearch(unittest.TestCase):

    def test_list_value_found(self):
        input = binary_search([-1, 0, 3, 5, 9, 12], 9)
        self.assertEqual(input, 4)

    def test_list_value_not_found(self):
        input = binary_search([-1, 0, 3, 5, 9, 12], 2)
        self.assertEqual(input, -1)

    def test_short_list_value_found(self):
        input = binary_search([999, 1000], 1000)
        self.assertEqual(input, 1)

    def test_short_list_value_not_found(self):
        input = binary_search([999, 1000], 888)
        self.assertEqual(input, -1)

    def test_one_list_value_not_found(self):
        input = binary_search([1], 2)
        self.assertEqual(input, -1)

    def test_one_list_value_found(self):
        input = binary_search([1], 1)
        self.assertEqual(input, 0)

    def test_three_list_value_found(self):
        input = binary_search([1, 2, 3], 3)
        self.assertEqual(input, 2)


if __name__ == "__main__":
    unittest.main()
