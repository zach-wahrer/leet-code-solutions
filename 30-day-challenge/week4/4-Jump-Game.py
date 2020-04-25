import unittest


# Recursive solution that times out on LeetCode
def can_finish_recursive(nums: list) -> bool:
    if len(nums) < 2:
        return True
    elif nums[0] == 0:
        return False

    for i in list(range(1, nums[0] + 1))[::-1]:
        if can_finish(nums[i:]):
            return True

    return False


# O(n) time / O(1) space solution
def can_finish(nums: list) -> bool:
    current_jump = 1
    for num in nums[:-1]:
        current_jump = max(current_jump - 1, num)
        if not current_jump:
            return False

    return True


class TestJumpToFinish(unittest.TestCase):
    def test_23114(self):
        self.assertTrue(can_finish([2, 3, 1, 1, 4]))

    def test_32104(self):
        self.assertFalse(can_finish([3, 2, 1, 0, 4]))


if __name__ == "__main__":
    unittest.main()
