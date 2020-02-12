import unittest


def duplicate_zeros(arr: list) -> None:
    pass


class TestDuplicateZeros(unittest.TestCase):

    def test_10230450(self):
        input = duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])
        self.assertEqual(input, [1, 0, 0, 2, 3, 0, 0, 4])

    def test_123(self):
        input = duplicate_zeros([1, 2, 3])
        self.assertEqual(input, [1, 2, 3])

    def test_8(self):
        input = duplicate_zeros([8])
        self.assertEqual(input, [8])

    def test_10(self):
        input = duplicate_zeros([1, 0])
        self.assertEqual(input, [1, 0])

    def test_8(self):
        input = duplicate_zeros([0])
        self.assertEqual(input, [0])

    def test_0909(self):
        input = duplicate_zeros([0, 9, 0, 9])
        self.assertEqual(input, [0, 0, 0, 0])

    def test_blank(self):
        input = duplicate_zeros([])
        self.assertEqual(input, [])


if __name__ == "__main__":
    unittest.main()
