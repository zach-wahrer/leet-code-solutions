import unittest


# Solution using Python built in shuffle
class Solution_Built:

    def __init__(self, nums):
        self._original_nums = nums

    def reset(self):
        return self._original_nums

    def shuffle(self):
        import random
        shuffled = self._original_nums.copy()
        random.shuffle(shuffled)
        return shuffled


# Solution using implimented shuffle
class Solution:

    def __init__(self, nums):
        self._original_nums = nums

    def reset(self):
        return self._original_nums

    def shuffle(self):
        import random
        shuffled = self._original_nums.copy()
        length = len(shuffled)
        for i in range(length):
            random_index = random.randint(0, length - 1)
            shuffled[i], shuffled[random_index] = shuffled[random_index], shuffled[i]
        return shuffled


class TestShuffle(unittest.TestCase):
    def test_123(self):
        obj = Solution([1, 2, 3])
        self.assertEqual(obj.reset(), [1, 2, 3])
        self.assertNotEqual(obj.shuffle(), [])
        self.assertEqual(obj.reset(), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
