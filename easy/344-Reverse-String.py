import unittest


def reverse_string_easy(s: list) -> None:
    s.reverse()


def reverse_string(s: list) -> None:
    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
        s[p1], s[p2] = s[p2], s[p1]
        p1 += 1
        p2 -= 1


class TestReverseString(unittest.TestCase):

    def test_hello(self):
        input = ["h", "e", "l", "l", "o"]
        reverse_string(input)
        output = ["o", "l", "l", "e", "h"]
        self.assertEqual(input, output)

    def test_hello(self):
        input = ["H", "a", "n", "n", "a", "h"]
        reverse_string(input)
        output = ["h", "a", "n", "n", "a", "H"]
        self.assertEqual(input, output)

    def test_blank(self):
        input = []
        reverse_string(input)
        output = []
        self.assertEqual(input, output)

    def test_a(self):
        input = ['a']
        reverse_string(input)
        output = ['a']
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
