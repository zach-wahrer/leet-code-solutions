import unittest


def search_pos_rotated_array(nums: list, target: int) -> int:
    pass


class SearchRotatedSortedArray(unittest.TestCase):

    def test_4567012_0_found(self):
        input = search_pos_rotated_array([4, 5, 6, 7, 0, 1, 2, 3], 0)
        self.assertEqual(input, 4)

    def test_4567012_3_not_found(self):
        input = search_pos_rotated_array([4, 5, 6, 7, 0, 1, 2, 3], 3)
        self.assertEqual(input, -1)

    def test_len_1_found(self):
        input = search_pos_rotated_array([1], 1)
        self.assertEqual(input, 0)

    def test_len_1_not_found(self):
        input = search_pos_rotated_array([1], 2)
        self.assertEqual(input, -1)

    def test_len_2_found(self):
        input = search_pos_rotated_array([2, 1], 1)
        self.assertEqual(input, 1)

    def test_len_2_not_found(self):
        input = search_pos_rotated_array([2, 1], 0)
        self.assertEqual(input, -1)

    def test_123_1_found(self):
        input = search_pos_rotated_array([1, 2, 3], 1)
        self.assertEqual(input, 0)

    def test_123_4_not_found(self):
        input = search_pos_rotated_array([1, 2, 3], 4)
        self.assertEqual(input, -1)

    def test_12310_1_found(self):
        input = search_pos_rotated_array([1, 2, 3, -1, 0], -1)
        self.assertEqual(input, 3)

    def test_12310_2_found(self):
        input = search_pos_rotated_array([1, 2, 3, -1, 0], 2)
        self.assertEqual(input, 1)


if __name__ == "__main__":
    unittest.main()
