import unittest


def find_25_int(arr: list) -> int:
    pass


class TestFind25(unittest.TestCase):

    def test_6(self):
        self.assertEqual(find_25_int([1, 2, 2, 6, 6, 6, 6, 7, 10]), 6)

    def test_one_item(self):
        self.assertEqual(find_25_int([0]), 0)

    def test_8(self):
        self.assertEqual(find_25_int([8, 8, 8, 8, 8]), 8)

    def test_2(self):
        self.assertEqual(find_25_int([1, 2, 2, 3, 4, 5, 6]), 8)


if __name__ == '__main__':
    unittest.main()
