'''
Psudocode:

'''

import unittest


def find_prefix(strs: list) -> str:
    pass


class TestPrefix(unittest.TestCase):

    def test_fl(self):
        input = find_prefix(["flower"], ["flow"], ["flight"])
        output = "fl"
        self.assertEqual(input, output)

    def test_none(self):
        input = find_prefix(["dog"], ["racecar"], ["car"])
        output = ""
        self.assertEqual(input, output)

    def test_white(self):
        input = find_prefix(["whitehouse"], ["whiteboard"])
        output = "white"
        self.assertEqual(input, output)

    def test_pain(self):
        input = find_prefix(["painful"], ["pain killer"], ["pain management"])
        output = "pain"
        self.assertEqual(input, output)

    def test_z(self):
        input = find_prefix(["zach"], ["zebra"], ["zoot"], ["zoo"])
        output = "z"
        self.assertEqual(input, output)
