import unittest


def num_ways(s: str) -> int:
    pass


class TestNumberOfWays(unittest.TestCase):

    def test_12(self):
        self.assertEqual(num_ways('12'), 2)

    def test_226(self):
        self.assertEqual(num_ways('226'), 3)


if __name__ == "__main__":
    unittest.main()
