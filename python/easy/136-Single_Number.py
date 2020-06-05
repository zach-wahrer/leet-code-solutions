'''
Psudocode:
    List:
        Go through input numbers
            Add number to unique list if it isn't there
            Remove if it is

    Hash:
        Go through input numbers
            Add numbers to unique dict if it isn't there
            Remove if it is

'''

import unittest


# Hash algorithm
def find_single_int(nums: list) -> int:
    uniques = dict()
    for number in nums:
        if number not in uniques:
            uniques[number] = None
        else:
            uniques.pop(number)
    return uniques.popitem()[0]


# List algorithm
def find_single_int_list(nums: list) -> int:
    uniques = list()
    for number in nums:
        if number not in uniques:
            uniques.append(number)
        else:
            uniques.remove(number)
    return uniques[0]


class TestSingleInt(unittest.TestCase):

    def test_221(self):
        input = find_single_int([2, 2, 1])
        output = 1
        self.assertEqual(input, output)

    def test_41212(self):
        input = find_single_int([4, 1, 2, 1, 2])
        output = 4
        self.assertEqual(input, output)

    def test_8151822(self):
        input = find_single_int([8, 1, 5, 1, 8, 2, 2])
        output = 5
        self.assertEqual(input, output)

    def test_44876181227(self):
        input = find_single_int([4, 4, 8, 7, 6, 1, 8, 1, 2, 2, 7])
        output = 6
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
