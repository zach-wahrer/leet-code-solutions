import unittest


# O(n) time/space solution
def is_valid(s: str) -> bool:

    stack = []
    for char in s:
        if char == '(' or char == '*':
            stack.append(char)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    stack = []
    for char in s[::-1]:
        if char == ')' or char == '*':
            stack.append(char)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    return True


class TestValidParenthesis(unittest.TestCase):
    def test_complex(self):
        self.assertTrue(is_valid(
            "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))

    def test_wildcards(self):
        self.assertTrue(is_valid("(((******)))"))

    def test_unmatched(self):
        self.assertFalse(is_valid(")("))

    def test_wild_as_right(self):
        self.assertTrue(is_valid("(*()"))

    def test_simple(self):
        self.assertTrue(is_valid("()"))

    def test_wild_as_empty(self):
        self.assertTrue(is_valid("(*)"))

    def test_wild_as_left(self):
        self.assertTrue(is_valid("(*))"))

    def test_empty(self):
        self.assertTrue(is_valid(""))

    def test_empty2(self):
        self.assertTrue(is_valid("*"))

    def test_missing_right(self):
        self.assertFalse(is_valid("(()"))

    def test_no_left(self):
        self.assertFalse(is_valid(")"))

    def test_missing_left(self):
        self.assertFalse(is_valid("*))"))


if __name__ == "__main__":
    unittest.main()
