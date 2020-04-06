import unittest


def group_anagrams(strs: list) -> list:
    pass


class TestGroup(unittest.TestCase):
    def test_six(self):
        input = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        output = [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ]
        self.assertEqual(input, output)
