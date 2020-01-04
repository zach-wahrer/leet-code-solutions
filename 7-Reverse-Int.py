'''
Psudocode:
    List comprehension to separate int to list
    Reverse list
    Combine back to int, adding neg if original number was neg
    If final value is > 2**31-1 or < -2**31, output 0
'''

import unittest


def reverse_int(x: int) -> int:
    number = [int(i) for i in str(abs(x))[::-1]]
    final_number = int(''.join(map(str, number)))
    if final_number not in range(-2**31, 2**31 - 1):
        return 0
    elif x < 0:
        return final_number * -1
    else:
        return final_number


class TestReverse(unittest.TestCase):

    def test_123(self):
        input = reverse_int(123)
        output = 321
        self.assertEqual(input, output)

    def test_minus123(self):
        input = reverse_int(-123)
        output = -321
        self.assertEqual(input, output)

    def test_8800(self):
        input = reverse_int(8800)
        output = 88
        self.assertEqual(input, output)

    def test_minus1000(self):
        input = reverse_int(-1000)
        output = -1
        self.assertEqual(input, output)

    def test_120(self):
        input = reverse_int(120)
        output = 21
        self.assertEqual(input, output)

    def test_2_31(self):
        input = reverse_int(2**31)
        output = 0
        self.assertEqual(input, output)

    def test_minus2_31_minus1(self):
        input = reverse_int(-2**31 - 1)
        output = 0
        self.assertEqual(input, output)

    def test_1534236469(self):
        input = reverse_int(1534236469)
        output = 0
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
