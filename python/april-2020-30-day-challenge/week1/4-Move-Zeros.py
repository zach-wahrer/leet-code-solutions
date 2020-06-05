import unittest


# O(n) time / O(1) space solution
def move_zeros(nums: list) -> None:
    if len(nums) < 2:
        return

    p1, p2 = 0, 1
    while p2 < len(nums) and p1 < len(nums):
        if nums[p1] == 0:
            while p2 < len(nums) - 1 and nums[p2] == 0:
                p2 += 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
        p2 += 1
        p1 += 1


class TestMoveZeros(unittest.TestCase):
    def test_long(self):
        nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
        move_zeros(nums)
        self.assertEqual(nums, [4, 2, 4, 3, 5, 1, 0, 0, 0, 0])

    def test_010312(self):
        nums = [0, 1, 0, 3, 12]
        move_zeros(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_00(self):
        nums = [0, 0]
        move_zeros(nums)
        self.assertEqual(nums, [0, 0])

    def test_1(self):
        nums = [1]
        move_zeros(nums)
        self.assertEqual(nums, [1])

    def test_01(self):
        nums = [0, 1]
        move_zeros(nums)
        self.assertEqual(nums, [1, 0])

    def test_10(self):
        nums = [1, 0]
        move_zeros(nums)
        self.assertEqual(nums, [1, 0])

    def test_21(self):
        nums = [2, 1]
        move_zeros(nums)
        self.assertEqual(nums, [2, 1])


if __name__ == "__main__":
    unittest.main()
