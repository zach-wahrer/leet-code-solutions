'''
Psudocode:
    Create dict for roman: int values
    Iterate over string, summing number
    If char is I, X, or C, look ahead to see if next letter is valued less
        If true, subtract I, X, or C from it
'''

import unittest


def convert_roman(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    out_number = 0
    s_len = len(s)
    for posistion, char in enumerate(s):
        char_value = values[char]
        if posistion + 1 < s_len:
            if char_value < values[s[posistion + 1]]:
                out_number -= char_value
            else:
                out_number += char_value
        else:
            out_number += char_value
    return out_number


class TestRomanConversion(unittest.TestCase):

    def test_III(self):
        input = convert_roman('III')
        output = 3
        self.assertEqual(input, output)

    def test_IV(self):
        input = convert_roman('IV')
        output = 4
        self.assertEqual(input, output)

    def test_IX(self):
        input = convert_roman('IX')
        output = 9
        self.assertEqual(input, output)

    def test_LVIII(self):
        input = convert_roman('LVIII')
        output = 58
        self.assertEqual(input, output)

    def test_MDCL(self):
        input = convert_roman('MDCL')
        output = 1650
        self.assertEqual(input, output)

    def test_CMI(self):
        input = convert_roman('CMI')
        output = 901
        self.assertEqual(input, output)

    def test_MMMCMXCIX(self):
        input = convert_roman('MMMCMXCIX')
        output = 3999
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
