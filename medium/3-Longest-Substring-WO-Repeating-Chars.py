import unittest


# Naive - fails test_dvdf_3
def longest_sub_naive(s: str) -> int:
    substring = []
    counts = [0]
    for char in s:
        if char in substring:
            counts.append(len(substring))
            print(substring, counts[-1])
            substring.clear()
            substring.append(char)
        else:
            substring.append(char)

    if substring:
        counts.append(len(substring))
        print(substring, counts[-1])

    return max(counts)


def longest_sub(s: str) -> int:
    if len(s) < 2:
        return len(s)
    counts = [0]
    left = 0
    right = 1

    def move_window(left, right, counts):
        if right != len(s) - 1:
            while s[left] != s[right] and right < len(s) - 1:
                right += 1
            counts.append(right - left) if left == 0 else counts.append(right - left + 1)
            print(right - left)
            left += 1
            print(left, s[left], " : ", right, s[right])

            move_window(left, right, counts)

    move_window(left, right, counts)

    print(counts)
    return max(counts)


class TestLongestSubstring(unittest.TestCase):

    def test_dvdf_3(self):
        self.assertEqual(longest_sub('dvdf'), 3)
    #
    # def test_abcabcbb_3(self):
    #     self.assertEqual(longest_sub('abcabcbb'), 3)
    #
    # def test_bbbbb_1(self):
    #     self.assertEqual(longest_sub('bbbbb'), 1)
    #
    # def test_pwwkew_3(self):
    #     self.assertEqual(longest_sub('pwwkew'), 3)
    #
    # def test_blank_0(self):
    #     self.assertEqual(longest_sub(''), 0)
    #
    # def test_a_1(self):
    #     self.assertEqual(longest_sub('a'), 1)
    #
    # def test_ab_2(self):
    #     self.assertEqual(longest_sub('ab'), 2)
    #
    # def test_ab1ab1_3(self):
    #     self.assertEqual(longest_sub('ab1ab1'), 3)
    #
    # def test_aab_2(self):
    #     self.assertEqual(longest_sub('aab'), 2)


if __name__ == "__main__":
    unittest.main()
