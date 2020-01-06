'''
Psudocode:

'''

import unittest


def convert_roman(s: str) -> int:
    pass


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


if __name__ == '__main__':
    unittest.main()
