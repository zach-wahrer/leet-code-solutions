import unittest


def remove_dupes(nums: list) -> int:
    pass


class TestRemovingDuplicates(unittest.TestCase):

    def test_0011122334(self):
        input_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        new_list_len = remove_dupes(input_list)
        self.assertEqual(new_list_len, 5)
        self.assertEqual(input_list, [0, 1, 2, 3, 4, 2, 2, 3, 3, 4])


if __name__ == "__main__":
    unittest.main()
