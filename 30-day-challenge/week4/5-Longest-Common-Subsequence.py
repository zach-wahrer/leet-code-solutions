import unittest


def longest_common_subseq(text1: str, text2: str) -> int:
    pass


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_abcde_ace(self):
        text1 = "abcde"
        text2 = "ace"
        self.assertEqual(longest_common_subseq(text1, text2), 3)

    def test_abc_abc(self):
        text1 = "abc"
        text2 = "abc"
        self.assertEqual(longest_common_subseq(text1, text2), 3)

    def test_abc_def(self):
        text1 = "abc"
        text2 = "def"
        self.assertEqual(longest_common_subseq(text1, text2), 0)


if __name__ == "__main__":
    unittest.main()
