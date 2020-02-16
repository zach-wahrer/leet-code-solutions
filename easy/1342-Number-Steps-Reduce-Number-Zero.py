import unittest


def reduce_num_to_zero(num: int) -> int:
    pass


class TestReduceToZero(unittest.TestCase):

    def test_14(self):
        input = reduce_num_to_zero(14)
        self.assertEqual(input, 6)

    def test_8(self):
        input = reduce_num_to_zero(8)
        self.assertEqual(input, 4)

    def test_123(self):
        input = reduce_num_to_zero(123)
        self.assertEqual(input, 12)

    def test_blank(self):
        input = reduce_num_to_zero("")
        self.assertEqual(input, 0)

    def test_0(self):
        input = reduce_num_to_zero(0)
        self.assertEqual(input, 0)
