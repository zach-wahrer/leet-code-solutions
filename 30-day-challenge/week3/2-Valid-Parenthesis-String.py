import unittest


def is_valid(s: str) -> bool:

    def _scan_string(s: str, direction: str) -> list:
        stack = []

        for char in [char for char in s][::direction]:
            if char == "(":
                if ")" in stack:
                    stack.remove(")")
                elif "*" in stack:
                    stack.remove("*")
                else:
                    stack.append(char)
            elif char == ")":
                if "(" in stack:
                    stack.remove("(")
                elif "*" in stack:
                    stack.remove("*")
                else:
                    stack.append(")")
            else:
                if "(" in stack and len(stack) > 1:
                    stack.remove("(")
                else:
                    stack.append(char)

        if "*" in stack:
            stack.remove("*")

        return stack

    if not _scan_string(s, 1) or not _scan_string(s, -1):
        return True

    return False


class TestValidParenthesis(unittest.TestCase):
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
