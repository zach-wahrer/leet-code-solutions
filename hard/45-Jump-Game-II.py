import unittest


def min_jumps(nums: list) -> int:
    pass


class TestMinJumps(unittest.TestCase):

    def test_23114(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4]), 2)

    def test_1111(self):
        self.assertEqual(min_jumps([1, 1, 1, 1]), 3)

    def test_tricky(self):
        self.assertEqual(min_jumps([5, 8, 1, 1, 1, 1, 1, 1, 1, 1]), 2)


if __name__ == "__main__":
    unittest.main()
