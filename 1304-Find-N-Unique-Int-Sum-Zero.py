'''
Psudocode:
    Make a list from 1:n
    Replace list[0] with the sum of remaining list
'''

import unittest


def unique_ints(number: int) -> list:
    numbers_list = list(range(number))
    numbers_list[0] = sum(numbers_list[1:]) * -1
    return numbers_list


class TestUniqueList(unittest.TestCase):

    def test_5(self):
        input = sum(unique_ints(5))
        output = 0
        self.assertEqual(input, output)

    def test_3(self):
        input = sum(unique_ints(3))
        output = 0
        self.assertEqual(input, output)

    def test_1(self):
        input = sum(unique_ints(1))
        output = 0
        self.assertEqual(input, output)

    def test_47(self):
        input = sum(unique_ints(47))
        output = 0
        self.assertEqual(input, output)

    def test_1000(self):
        input = sum(unique_ints(1000))
        output = 0
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
