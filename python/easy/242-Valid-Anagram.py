import unittest


# Naive solution - O(n**2) - Doesn't pass test_multi_false
def is_anagram_naive(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    for char in s:
        if char not in t:
            return False

    return True


# Solution - O(n+m) time, O(n+m) space
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    def element_counter(string):
        counts = {}
        for char in string:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        return counts

    return element_counter(s) == element_counter(t)


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

    def test_multi_true(self):
        self.assertTrue(is_anagram('aaz', 'zaa'))

    def test_multi_false(self):
        self.assertFalse(is_anagram('azz', 'zaa'))

    def test_diff_len_false(self):
        self.assertFalse(is_anagram('abc', 'abcd'))


if __name__ == "__main__":
    unittest.main()
