import unittest


def first_unique(s: str) -> int:
    pass


class TestFirstUnique(unittest.TestCase):

    def test_leetcode(self):
        self.assertEqual(first_unique('leetcode'), 0)

    def test_loveleetcode(self):
        self.assertEqual(first_unique('loveleetcode'), 2)

    def test_blank(self):
        self.assertEqual(first_unique(''), -1)

    def test_aaaaaa(self):
        self.assertEqual(first_unique('aaaaaa'), -1)

    def test_z(self):
        self.assertEqual(first_unique('z'), 0)


if __name__ == "__main__":
    unittest.main()
