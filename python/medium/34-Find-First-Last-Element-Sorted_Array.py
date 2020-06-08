import unittest


def search_range(nums: list, target: int) -> list:
    pass


class TestSearchRange(unittest.TestCase):
    def test_found(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertEqual(search_range(nums, target), [3, 4])

    def test_not_found(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        self.assertEqual(search_range(nums, target), [-1, -1])

    def test_blank(self):
        nums = []
        target = 6
        self.assertEqual(search_range(nums, target), [-1, -1])

    def test_1_element_input_found(self):
        nums = [1]
        target = 1
        self.assertEqual(search_range(nums, target), [0, 0])

    def test_1_element_input_not_found(self):
        nums = [1]
        target = 3
        self.assertEqual(search_range(nums, target), [-1, -1])

    def test_2_element_input_found(self):
        nums = [2, 2]
        target = 2
        self.assertEqual(search_range(nums, target), [0, 1])

    def test_2_element_input_not_found(self):
        nums = [2, 2]
        target = 4
        self.assertEqual(search_range(nums, target), [-1, -1])

if __name__ == "__main__":
    unittest.main()
