import unittest


def single_num(nums: list) -> int:
    pass


class TestSingleNum(unittest.TestCase):

    def test_221(self):
        self.assertEqual(single_num([2, 2, 1]), 1)

    def test_41212(self):
        self.assertEqual(single_num([4, 1, 2, 1, 2]), 4)

    def test_0(self):
        self.assertEqual(single_num([0]), 0)


if __name__ == "__main__":
    unittest.main()
