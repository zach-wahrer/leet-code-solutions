"""
Psudocode:
    Read through string, incrementing L and R counts
    When counts are =, increment output count and zero L and R counts
    Continue

"""

import unittest


def splitter(s):
    count = {'L': 0, 'R': 0, 'T': 0}
    for c in s:
        count[c] += 1
        if count['L'] == count['R']:
            count['T'] += 1
            count['L'] = 0
            count['R'] = 0
    return count['T']


class TestSplit(unittest.TestCase):

    def test_RLRRLLRLRL(self):
        input = splitter('RLRRLLRLRL')
        output = 4
        self.assertEqual(input, output)

    def test_RLLLLRRRLR(self):
        input = splitter('RLLLLRRRLR')
        output = 3
        self.assertEqual(input, output)

    def test_LLLLRRRR(self):
        input = splitter('LLLLRRRR')
        output = 1
        self.assertEqual(input, output)

    def test_RLRRRLLRLL(self):
        input = splitter('RLRRRLLRLL')
        output = 2
        self.assertEqual(input, output)

    def test_RRLLRRLLRRLL(self):
        input = splitter('RRLLRRLLRRLL')
        output = 3
        self.assertEqual(input, output)

    def test_RRLLRRLLRRLRLL(self):
        input = splitter('RRLLRRLLRRLRLL')
        output = 3
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
