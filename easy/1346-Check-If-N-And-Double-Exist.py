import unittest


def check_double_of_n(arr: list) -> bool:
    pass


class TestDoubleN(unittest.TestCase):
    def test_10253(self):
        input = check_double_of_n([10, 2, 5, 3])
        self.assertTrue(input)

    def test_711411(self):
        input = check_double_of_n([7, 1, 14, 11])
        self.assertTrue(input)

    def test_3171(self):
        input = check_double_of_n([3, 1, 7, 11])
        self.assertFalse(input)

    def test_82(self):
        input = check_double_of_n([8, 2])
        self.assertFalse(input)

    def test_12(self):
        input = check_double_of_n([1, 2])
        self.assertTrue(input)
