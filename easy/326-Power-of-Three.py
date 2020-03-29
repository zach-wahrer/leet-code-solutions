import unittest


def is_power_three(n: int) -> bool:
    pass


class TestPowerOfThree(unittest.TestCase):

    def test_27(self):
        self.assertTrue(is_power_three(27))

    def test_9(self):
        self.assertTrue(is_power_three(9))

    def test_0(self):
        self.assertFalse(is_power_three(0))

    def test_45(self):
        self.assertFalse(is_power_three(45))
