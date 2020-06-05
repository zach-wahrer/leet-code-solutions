'''
Psudocode:
    For each number in list
        Count digits, increment counter if even
'''

import unittest


def find_numbers(nums: list) -> int:
    even_count = 0
    for number in nums:
        if len(str(number)) % 2 == 0:
            even_count += 1
    return even_count


class TestEven_Nums(unittest.TestCase):

    def test_output_2(self):
        input = find_numbers([12, 345, 2, 6, 7896])
        output = 2
        self.assertEqual(input, output)

    def test_output_1(self):
        input = find_numbers([555, 901, 482, 1771])
        output = 1
        self.assertEqual(input, output)

    def test_output_0(self):
        input = find_numbers([1, 1, 0, 3, 333, 444])
        output = 0
        self.assertEqual(input, output)

    def test_output_5(self):
        input = find_numbers([11, 11, 33, 4444, 777777])
        output = 5
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
