import unittest


# Dynamic O(n*m) solution
def longest_common_subseq(text1: str, text2: str) -> int:
    len1 = len(text1)
    len2 = len(text2)

    memoize = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            if text1[i] == text2[j]:
                memoize[i][j] = memoize[i + 1][j + 1] + 1
            else:
                memoize[i][j] = max(memoize[i + 1][j], memoize[i][j + 1], memoize[i + 1][j + 1])

    return memoize[0][0]


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
