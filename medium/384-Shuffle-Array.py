import unittest


# Solution using Python built in shuffle
class Solution:

    def __init__(self, nums):
        self._original_nums = nums

    def reset(self):
        return self._original_nums

    def shuffle(self):
        import random
        shuffled = self._original_nums.copy()
        random.shuffle(shuffled)
        return shuffled


class TestShuffle(unittest.TestCase):
    def test_123(self):
        obj = Solution([1, 2, 3])
        self.assertEqual(obj.reset(), [1, 2, 3])
        self.assertNotEqual(obj.shuffle(), [1, 2, 3])
        self.assertEqual(obj.reset(), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
