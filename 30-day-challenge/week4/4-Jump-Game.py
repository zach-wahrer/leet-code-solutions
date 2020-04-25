import unittest


def can_finish(nums: list) -> bool:
    pass


class TestJumpToFinish(unittest.TestCase):
    def test_23114(self):
        self.assertTrue(can_finish([2, 3, 1, 1, 4]))

    def test_32104(self):
        self.assertFalse(can_finish([3, 2, 1, 0, 4]))
