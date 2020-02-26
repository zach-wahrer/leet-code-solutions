import unittest


def longest_sub(s: str) -> int:
    pass


class TestLongestSubstring(unittest.TestCase):

    def test_abcabcbb_3(self):
        self.assertEqual(longest_sub(['abcabcbb']), 3)

    def test_bbbbb_1(self):
        self.assertEqual(longest_sub(['bbbbb']), 1)

    def test_pwwkew_3(self):
        self.assertEqual(longest_sub(['pwwkew']), 3)
