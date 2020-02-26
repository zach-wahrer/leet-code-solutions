import unittest


def is_anagram(s: str, t: str) -> bool:
    pass


class TestAnagram(unittest.TestCase):

    def test_anagram_true(self):
        self.assertTrue(is_anagram('anagram', 'nagaram'))

    def test_rat_false(self):
        self.assertFalse(is_anagram('rat', 'car'))

    def test_blank_true(self):
        self.assertTrue(is_anagram('', ''))

    def test_one_true(self):
        self.assertTrue(is_anagram('o', 'o'))

    def test_one_false(self):
        self.assertFalse(is_anagram('o', 'p'))

    def test_op_true(self):
        self.assertTrue(is_anagram('op', 'po'))
