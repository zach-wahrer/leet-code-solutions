import unittest


def group_anagrams(strs: list) -> list:
    pass


class TestAnagramsGrouping(unittest.TestCase):
    def test_3_groups(self):
        input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ]
        self.assertEqual(group_anagrams(input), output)

    def test_1_group(self):
        input = ["eat", "tea"]
        output = [["ate", "tea"]]
        self.assertEqual(group_anagrams(input), output)

    def test_2_groups(self):
        input = ["cat", "hat", "tha"]
        output = [["cat"], ["hat", "tha"]]
        self.assertEqual(group_anagrams(input), output)
