import unittest


def find_majority(nums: list) -> int:
    pass


class TestFindMajority(unittest.TestCase):

    def test_323(self):
        self.assertEqual(find_majority([3, 2, 3]), 3)

    def test_2211122(self):
        self.assertEqual(find_majority([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
