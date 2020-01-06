'''
Psudocode:
    Step through string
        Increment open braces
        Decrement on closed braces
    Check that all counts are back to 0, return true

    V2:
    Mirror the string (changing opens to closes)
    Check mirror vs orig
'''

import unittest


def valid_paren(s: str) -> bool:
    if s == "":
        return True
    if len(s) % 2 != 0:
        return False

    stack = list()
    open_chars = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in open_chars:
            stack.append(char)
        else:
            if stack == []:
                return False
            if open_chars[stack[-1]] == char:
                stack.pop()
            else:
                return False

    return stack == []


def valid_paren_wrong_1(s: str) -> bool:
    '''Doesn't work for strings that are valid, but not symmetrical.'''
    if s == "":
        return True
    if len(s) % 2 != 0:
        return False

    mirror_string = ''
    mirror_char = {'(': ')', ')': '(', '{': '}', '}': "{", '[': ']', ']': '['}
    for char in s:
        mirror_string += mirror_char[char]
    return s == mirror_string[::-1]


def valid_paren_wrong_0(s: str) -> bool:
    '''Doesn't work for out of sequence closes.'''
    if len(s) % 2 != 0:
        return False
    counts = {'(': 0, ')': 0, '{': 0, '}': 0, '[': 0, ']': 0}
    # Check for equal numbers of opens and closes
    for char in s:
        counts[char] += 1
    for pairs in zip(list(counts.values())[0::2], list(counts.values())[1::2]):
        if pairs[0] - pairs[1] != 0:
            return False
    return True


class TestParentheses(unittest.TestCase):

    def test_closed_para(self):
        self.assertTrue(valid_paren('()'))

    def test_closed_para_braces(self):
        self.assertTrue(valid_paren('()[]{}'))

    def test_unclosed_para(self):
        self.assertFalse(valid_paren('(]'))

    def test_invalid_para(self):
        self.assertFalse(valid_paren('([)]'))

    def test_nested(self):
        self.assertTrue(valid_paren('{[]}'))

    def test_nested_2(self):
        self.assertTrue(valid_paren('({[()]})'))

    def test_empty(self):
        self.assertTrue(valid_paren(''))

    def test_odd(self):
        self.assertFalse(valid_paren('([)'))

    def test_open(self):
        self.assertFalse(valid_paren('(('))

    def test_closed_first(self):
        self.assertFalse(valid_paren('){'))


if __name__ == '__main__':
    unittest.main()
