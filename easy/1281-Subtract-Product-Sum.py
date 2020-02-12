"""
Psudocode:
    Get sum and product of input by looping through digits
    Subtract product from sum
    Return value

    Didn't think of numbers with 0 in them initally... Uh oh...
"""

import unittest


def diff_sum_product(n):
    num = list(str(n))
    sum = 0
    product = 0
    first = True
    for i in num:
        if first is True:
            product = int(i)
        else:
            product *= int(i)
        sum += int(i)
        first = False
    return product - sum


class TestNumber(unittest.TestCase):

    def test_234(self):
        input = diff_sum_product(234)
        output = 15
        self.assertEqual(input, output)

    def test_4421(self):
        input = diff_sum_product(4421)
        output = 21
        self.assertEqual(input, output)

    def test_52264(self):
        input = diff_sum_product(52264)
        output = 461
        self.assertEqual(input, output)

    def test_705(self):
        input = diff_sum_product(705)
        output = -12
        self.assertEqual(input, output)

    def test_600(self):
        input = diff_sum_product(600)
        output = -6
        self.assertEqual(input, output)

    def test_601(self):
        input = diff_sum_product(601)
        output = -7
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
