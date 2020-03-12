import unittest


# Recursive Brute Force Solution - Times out on LeetCode
def can_finish(nums: list) -> bool:
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


if __name__ == "__main__":
    unittest.main()
