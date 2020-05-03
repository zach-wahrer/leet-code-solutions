import unittest


def num_1_bits(n: int) -> int:
    pass


class TestNum1Bits(unittest.TestCase):
    def test_11(self):
        self.assertEqual(num_1_bits(11), 3)

    def test_128(self):
        self.assertEqual(num_1_bits(128), 1)

    def test_4294967293(self):
        self.assertEqual(num_1_bits(4294967293), 31)
