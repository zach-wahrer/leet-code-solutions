'''
Psudocode:
    Iterate through strings, checking against next string in sequence
        If match, check against next string
        If not, return ""
    If at last string and still match, return it
'''

import unittest


def find_prefix(strs: list) -> str:
    output = ""
    for row_chars in zip(* [string for string in strs]):
        if row_chars.count(row_chars[0]) == len(row_chars):
            output += row_chars[0]
        else:
            return output
    return output


class TestPrefix(unittest.TestCase):

    def test_fl(self):
        input = find_prefix(["flower", "flow", "flight"])
        output = "fl"
        self.assertEqual(input, output)

    def test_none_0(self):
        input = find_prefix(["dog", "racecar", "car"])
        output = ""
        self.assertEqual(input, output)

    def test_white(self):
        input = find_prefix(["whitehouse", "whiteboard"])
        output = "white"
        self.assertEqual(input, output)

    def test_pain(self):
        input = find_prefix(["painful", "pain killer", "pain management"])
        output = "pain"
        self.assertEqual(input, output)

    def test_z(self):
        input = find_prefix(["zach", "zebra", "zoot", "zoo"])
        output = "z"
        self.assertEqual(input, output)

    def test_none_1(self):
        input = find_prefix(["hi", "hello", "hey", "bye"])
        output = ""
        self.assertEqual(input, output)

    def test_all(self):
        input = find_prefix(["all", "all", "all"])
        output = "all"
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
