import unittest


def move_zeros(nums: list) -> None:
    pass


class TestMoveZeros(unittest.TestCase):
    def test_010312(self):
        nums = [0, 1, 0, 3, 12]
        move_zeros(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])
