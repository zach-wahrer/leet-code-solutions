import unittest


# O(n log n) time / O(n) space solution
def group_anagrams(strs: list) -> list:
    words_seen = {}
    for word in strs:
        key = tuple(sorted(word))
        if key in words_seen:
            words_seen[key].append(word)
        else:
            words_seen[key] = [word]

    return list(words_seen.values())


class TestAnagramsGrouping(unittest.TestCase):
    def test_3_groups(self):
        input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]
        self.assertEqual(group_anagrams(input), output)

    def test_1_group(self):
        input = ["eat", "tea"]
        output = [["eat", "tea"]]
        self.assertEqual(group_anagrams(input), output)

    def test_2_groups(self):
        input = ["cat", "hat", "tha"]
        output = [["cat"], ["hat", "tha"]]
        self.assertEqual(group_anagrams(input), output)


if __name__ == "__main__":
    unittest.main()
