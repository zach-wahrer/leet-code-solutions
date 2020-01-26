'''
Psudocode:
    Brute:
    Iterate through the loop in place
    If we find a 0, delete that element, increment a counter
    When we get to the end, add counter's worth of 0s.
'''

import unittest


# O(n^2) - Fails some cases
def move_zeros(nums: list) -> None:
    for i, num in enumerate(nums):
        if num == 0:
            nums.pop(i)
            nums.append(0)
    return nums


class TestMoveZeros(unittest.TestCase):

    def test_010312(self):
        input = move_zeros([0, 1, 0, 3, 12])
        output = [1, 3, 12, 0, 0]
        self.assertEqual(input, output)

    def test_blank(self):
        input = move_zeros([])
        output = []
        self.assertEqual(input, output)

    def test_01(self):
        input = move_zeros([0, 1])
        output = [0, 1]
        self.assertEqual(input, output)

    def test_01(self):
        input = move_zeros([1])
        output = [1]
        self.assertEqual(input, output)

    def test_456000(self):
        input = move_zeros([4, 5, 6, 0, 0, 0])
        output = [4, 5, 6, 0, 0, 0]
        self.assertEqual(input, output)

    def test_90909099(self):
        input = move_zeros([9, 0, 9, 0, 9, 0, 9, 9])
        output = [9, 9, 9, 9, 9, 0, 0, 0]
        self.assertEqual(input, output)

    def test_001(self):
        input = move_zeros([0, 0, 1])
        output = [1, 0, 0]
        self.assertEqual(input, output)

    def test_0001(self):
        input = move_zeros([0, 0, 0, 1])
        output = [1, 0, 0, 0]
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
