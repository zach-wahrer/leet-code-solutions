import unittest


def decompress_list(nums: list) -> list:
    pass


class TestDecompress(unittest.TestCase):

    def test_1234(self):
        input = decompress_list([1, 2, 3, 4])
        self.assertEqual(input, [2, 4, 4, 4])

    def test_1123(self):
        input = decompress_list([1, 1, 2, 3])
        self.assertEqual(input, [1, 3, 3])

    def test_11(self):
        input = decompress_list([1, 1])
        self.assertEqual(input, [1])
