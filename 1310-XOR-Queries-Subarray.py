'''
Psudocode:
    Iterate through queries, calling xor function
    Return list of answers

    For xor function, get range from query
    If > 2, loop through, doing xor each time
    Else, just do xor
'''

import unittest


def xor_query(arr: list, queries: list) -> list:
    pass


class XorTest(unittest.TestCase):

    def test_1348(self):
        input = xor_query([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]])
        output = [2, 7, 14, 8]
        self.assertEqual(input, output)

    def test_48210(self):
        input = xor_query([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]])
        output = [8, 0, 4, 4]
        self.assertEqual(input, output)

    def test_0123456789(self):
        input = xor_query([i for i in range(10)], [[0, 9], [1, 5],
                                                   [8, 9], [0, 0]])
        output = [1, 1, 1, 0]
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
