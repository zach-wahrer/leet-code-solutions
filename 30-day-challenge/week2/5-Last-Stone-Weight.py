import unittest


def smash_stones(stones: list) -> int:
    pass


class TestStones(unittest.TestCase):
    def test_274181(self):
        self.assertEqual(smash_stones([2, 7, 4, 1, 8, 1]), 1)

    def test_22(self):
        self.assertEqual(smash_stones([2, 2]), 0)

    def test_222(self):
        self.assertEqual(smash_stones([2, 2, 2]), 1)


if __name__ == "__main__":
    unittest.main()
