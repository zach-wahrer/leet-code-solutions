import unittest


def is_happy(n: int) -> bool:
    pass


class TestIsHappy(unittest.TestCase):

    def test_19(self):
        self.assert_True(is_happy(19))

    def test_1(self):
        self.assert_True(is_happy(1))

    def test_15(self):
        self.assert_False(is_happy(15))

    def test_4(self):
        self.assert_False(is_happy(4))
