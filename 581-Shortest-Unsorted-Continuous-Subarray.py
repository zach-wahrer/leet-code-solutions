'''
Psudocode:

'''

import unittest


def shortest_subarray(nums: list) -> int:
    pass


class TestShortestSubarray(unittest.TestCase):

    def test_264810915(self):
        input = shortest_subarray([2, 6, 4, 8, 10, 9, 15])
        output = 5
        self.assertEqual(input, output)

    def test_19186432(self):
        input = shortest_subarray([1, 9, 18, 64, 32])
        output = 2
        self.assertEqual(input, output)

    def test_987654(self):
        input = shortest_subarray([9, 7, 8, 7, 6, 5, 4])
        output = 7
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
