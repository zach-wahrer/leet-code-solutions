'''
Psudocode:
    Convert list to a string, then int
    Add 1
    Convert int to string, then split to list
'''

import unittest


def plus_one(digits: list) -> list:
    number = ""
    for digit in digits:
        number += str(digit)
    number = int(number) + 1
    out_list = []
    for digit in str(number):
        out_list.append(int(digit))
    return out_list


class TestPlusOne(unittest.TestCase):

    def test_123(self):
        input = plus_one([1, 2, 3])
        output = [1, 2, 4]
        self.assertEqual(input, output)

    def test_0999(self):
        input = plus_one([0, 9, 9, 9])
        output = [1, 0, 0, 0]
        self.assertEqual(input, output)

    def test_1(self):
        input = plus_one([1])
        output = [2]
        self.assertEqual(input, output)

    def test_4321(self):
        input = plus_one([4, 3, 2, 1])
        output = [4, 3, 2, 2]
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
