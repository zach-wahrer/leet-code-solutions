'''
Psudocode:

'''

import unittest


def how_many_ways(n: int) -> int:
    pass


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
        output = 4
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
