import unittest


def how_many_ways(n: int) -> int:

    def _climb(remaining_stairs, steps):
        if remaining_stairs == 0:
            return 1

        if remaining_stairs < 0:
            return 0

        return _climb(remaining_stairs - 1, 1) + _climb(remaining_stairs - 2, 2)

    return _climb(n, 1)


class TestWaysToClimb(unittest.TestCase):

    def test_2(self):
        input = how_many_ways(2)
        output = 2
        self.assertEqual(input, output)

    def test_3(self):
        input = how_many_ways(3)
        output = 3
        self.assertEqual(input, output)

    def test_4(self):
        input = how_many_ways(4)
        output = 5
        self.assertEqual(input, output)

    def test_1(self):
        input = how_many_ways(1)
        output = 1
        self.assertEqual(input, output)

    def test_38(self):
        input = how_many_ways(38)
        output = 63245986
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
