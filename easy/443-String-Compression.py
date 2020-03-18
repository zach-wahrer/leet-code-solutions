import unittest


def compress_string(chars: list) -> int:
    pass


class TestCompress(unittest.TestCase):

    def test_a2b2c3(self):
        string = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
        input = compress_string(string)
        self.assertEqual((input, string), (6, ['a', '2', 'b', '2', 'c', '3', 'c']))

    def test_a(self):
        string = ['a']
        input = compress_string(string)
        self.assertEqual((input, string), (1, ['a']))

    def test_large(self):
        string = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        input = compress_string(string)
        self.assertEqual(
            (input, string), (4, ["a", "b", "1", "2", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))


if __name__ == '__main__':
    unittest.main()
