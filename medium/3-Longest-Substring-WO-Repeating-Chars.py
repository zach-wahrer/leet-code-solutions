from collections import deque
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

# Recursive moving window - fails most tests


def longest_sub_recursive(s: str) -> int:
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
            print(right - left, ":", left, s[left], "-", right, s[right])
            left += 1
            print("Sending to recursive: ", left, s[left], " : ", right, s[right])

            move_window(left, right, counts)

    move_window(left, right, counts)

    print(counts)
    return max(counts)


# Deque solution WORKS!!! O(n**2) solution, O(n) space
def longest_sub(s: str) -> int:

    if len(s) < 2:
        return len(s)

    char_deque = deque()
    char_deque.append(s[0])
    counts = [0]

    for char in s[1:]:
        if char == char_deque[0]:
            counts.append(len(char_deque))
            char_deque.popleft()
            char_deque.append(char)
        elif char in char_deque:
            counts.append(len(char_deque))
            for i in range(char_deque.index(char) + 1):
                char_deque.popleft()
            char_deque.append(char)
        else:
            char_deque.append(char)

    if char_deque:
        counts.append(len(char_deque))

    return max(counts)


# Deque solution with set lookups WORKS!!! O(n) solution, O(n) space
def longest_sub_linear(s: str) -> int:

    if len(s) < 2:
        return len(s)

    def catalog(item, char_deque, lookup_set):
        char_deque.append(item)
        lookup_set.add(item)

    char_deque = deque()
    lookup = set()
    catalog(s[0], char_deque, lookup)
    counts = [0]

    for char in s[1:]:
        if char == char_deque[0]:
            counts.append(len(char_deque))
            char_deque.popleft()
            catalog(char, char_deque, lookup)
        elif char in lookup:
            counts.append(len(char_deque))
            for i in range(char_deque.index(char) + 1):
                lookup.remove(char_deque.popleft())
            catalog(char, char_deque, lookup)
        else:
            catalog(char, char_deque, lookup)

    if char_deque:
        counts.append(len(char_deque))

    return max(counts)


# Sliding window from a solution on LeetCode
def longest_sub_leet(s: str) -> int:
    if len(s) < 2:
        return len(s)
    uniques = set()

    pos = 0
    current_max = 0

    for i in range(len(s)):
        while pos < len(s) and s[pos] not in uniques:
            uniques.add(s[pos])
            pos += 1
        current_max = max(current_max, len(uniques))
        uniques.remove(s[i])

    return current_max


class TestLongestSubstring(unittest.TestCase):

    def test_dvdf_3(self):
        self.assertEqual(longest_sub('dvdf'), 3)

    def test_abcabcbb_3(self):
        self.assertEqual(longest_sub('abcabcbb'), 3)

    def test_bbbbb_1(self):
        self.assertEqual(longest_sub('bbbbb'), 1)

    def test_pwwkew_3(self):
        self.assertEqual(longest_sub('pwwkew'), 3)

    def test_blank_0(self):
        self.assertEqual(longest_sub(''), 0)

    def test_a_1(self):
        self.assertEqual(longest_sub('a'), 1)

    def test_ab_2(self):
        self.assertEqual(longest_sub('ab'), 2)

    def test_ab1ab1_3(self):
        self.assertEqual(longest_sub('ab1ab1'), 3)

    def test_aab_2(self):
        self.assertEqual(longest_sub('aab'), 2)

    def test_cdd_2(self):
        self.assertEqual(longest_sub('cdd'), 2)

    def test_ohvhjdml_5(self):
        self.assertEqual(longest_sub('ohvhjdml'), 6)


if __name__ == "__main__":
    unittest.main()
