import unittest


def kth_element(nums: list, k: int) -> int:
    pass


class TestKthElement(unittest.TestCase):
    def test_short_5(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(kth_element(nums, 2), 5)

    def test_long_4(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        self.assertEqual(kth_element(nums, 4), 4)


if __name__ == "__main__":
    unittest.main()
