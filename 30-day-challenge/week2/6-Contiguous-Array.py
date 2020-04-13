import unittest


def max_contig_array(nums: list) -> int:
    pass


class TestMaxContiguousArray(unittest.TestCase):
    def test_01(self):
        self.assertEqual(max_contig_array([0, 1]), 2)

    def test_010(self):
        self.assertEqual(max_contig_array([0, 1, 0]), 2)

    def test_0(self):
        self.assertEqual(max_contig_array([0]), 1)

    def test_00(self):
        self.assertEqual(max_contig_array([0, 0]), 1)

    def test_00(self):
        self.assertEqual(max_contig_array([0, 1, 0, 1]), 4)
