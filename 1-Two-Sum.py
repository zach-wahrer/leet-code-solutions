'''
Psudocode:

'''

import unittest


def check_sums(nums: list, target: int) -> list:
    pass


class TestCheckSums(unittest.TestCase):

    def test_271115_9(self):
        input = check_sums([2, 7, 11, 15], 9)
        output = [0, 1]
        self.assertEqual(input, output)

    def test_1491312_17(self):
        input = check_sums([1, 4, 9, 13, 12], 17)
        output = [1, 3]
        self.assertEqual(input, output)

    def test_081616_32(self):
        input = check_sums([0, 8, 16, 16], 32)
        output = [2, 3]
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
