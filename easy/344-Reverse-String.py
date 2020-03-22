import unittest


def reverse_string(s: list) -> None:
    pass


class TestReverseString(unittest.TestCase):

    def test_hello(self):
        input = reverse_string(["h", "e", "l", "l", "o"])
        output = ["o", "l", "l", "e", "h"]
        self.assertEqual(input, output)

    def test_hello(self):
        input = reverse_string(["H", "a", "n", "n", "a", "h"])
        output = ["h", "a", "n", "n", "a", "H"]
        self.assertEqual(input, output)

    def test_blank(self):
        input = reverse_string([])
        output = []
        self.assertEqual(input, output)

    def test_a(self):
        input = reverse_string(['a'])
        output = ['a']
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
