import unittest


def is_valid(s: str) -> bool:
    pass


class TestValidParenthesis(unittest.TestCase):
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
