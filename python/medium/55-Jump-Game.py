import unittest


# Recursive Brute Force Solution - Times out on LeetCode
def can_finish_brute(nums: list) -> bool:
    finishes = []

    def _can_finish(forward_list):

        if len(forward_list) == 1 or len(forward_list) - 1 < forward_list[0]:
            finishes.append(True)
            return
        if forward_list[0] == 0:
            finishes.append(False)
            return

        for i in range(1, forward_list[0] + 1):
            _can_finish(forward_list[i:])

    _can_finish(nums)
    return True in finishes


# Better Brute Force Recursive Solution (still exceeds time limit)
def can_finish(nums: list) -> bool:

    def _can_finish(forward_list):

        if len(forward_list) == 1 or len(forward_list) - 1 < forward_list[0]:
            return True

        if forward_list[0] == 0:
            return False

        for i in range(1, forward_list[0] + 1):
            if _can_finish(forward_list[i:]):
                return True

    return _can_finish(nums)


def can_finish(nums: list) -> bool:
    current_jump = 1

    for num in nums[:-1]:
        current_jump = max(current_jump - 1, num)
        if not current_jump:
            return False

    return True


class TestFinish(unittest.TestCase):

    def test_23114(self):
        self.assertTrue(can_finish([2, 3, 1, 1, 4]))

    def test_32104(self):
        self.assertFalse(can_finish([3, 2, 1, 0, 4]))

    def test_3101(self):
        self.assertTrue(can_finish([3, 1, 0, 1]))

    def test_2101(self):
        self.assertFalse(can_finish([2, 1, 0, 1]))

    def test_000(self):
        self.assertFalse(can_finish([0, 0, 0]))

    def test_111(self):
        self.assertTrue(can_finish([1, 1, 1]))

    def test_1(self):
        self.assertTrue(can_finish([1]))

    def test_0(self):
        self.assertTrue(can_finish([0]))

    def test_large(self):
        self.assertTrue(can_finish([[2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4,
                                     6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]]))


if __name__ == "__main__":
    unittest.main()
