'''
Psudocode:
    Add both nums as bin()
    Output as str
'''

import unittest


def add_binary_nums(a: str, b: str) -> str:
    value = bin(int(a, 2) + int(b, 2))
    return value[2:]


class TestAddBinary(unittest.TestCase):

    def test_11_1(self):
        input = add_binary_nums("11", "1")
        output = "100"
        self.assertEqual(input, output)

    def test_1010_1011(self):
        input = add_binary_nums("1010", "1011")
        output = "10101"
        self.assertEqual(input, output)

    def test_1_1(self):
        input = add_binary_nums("1", "1")
        output = "10"
        self.assertEqual(input, output)

    def test_100000_0(self):
        input = add_binary_nums("100000", "0")
        output = "100000"
        self.assertEqual(input, output)

    def test_0_0(self):
        input = add_binary_nums("0", "0")
        output = "0"
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
