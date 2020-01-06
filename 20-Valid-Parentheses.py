'''
Psudocode:

'''

import unittest


def valid_paren(s: str) -> bool:
    pass


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


if __name__ == '__main__':
    unittest.main()
