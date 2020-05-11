import unittest


class Solution:
    def __init__(self, nums: list):
        self.unshuffled = nums

    def reset(self) -> list:
        return self.unshuffled

    def shuffle(self) -> list:
        from random import randint
        shuffled = self.unshuffled.copy()
        for i in range(len(shuffled)):
            rand_index = randint(0, len(shuffled) - 1)
            shuffled[i], shuffled[rand_index] = shuffled[rand_index], shuffled[i]
        return shuffled


class TestShuffleObject(unittest.TestCase):
    def test_object(self):
        test_list = [1, 2, 3]
        nums = Solution(test_list)
        self.assertNotEqual(nums.shuffle(), test_list)
        self.assertEqual(nums.reset(), test_list)
        self.assertNotEqual(nums.shuffle(), test_list)

    def test_blank(self):
        test_list = []
        nums = Solution(test_list)
        self.assertEqual(nums.shuffle(), test_list)
        self.assertEqual(nums.reset(), test_list)
        self.assertEqual(nums.shuffle(), test_list)


if __name__ == "__main__":
    unittest.main()
