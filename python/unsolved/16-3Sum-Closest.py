import unittest


# Solution
def closest_3sum(nums: list, target: int) -> int:
    from collections import deque

    def nearest_difference(target, original, new):
        # print(target, original, new)
        # print(abs(target - original), abs(target - new))
        if abs(target - original) < abs(target - new):

            return original
        return new

    if len(nums) <= 3:
        return sum(nums)

    nums.sort()
    queue = deque()

    for i in nums[:3:]:
        queue.append(i)
    closest = nearest_difference(target, float('-inf'), sum(queue))
    print(queue)

    for i in nums[3:]:

        queue.popleft()
        queue.append(i)
        closest = nearest_difference(target, closest, sum(queue))
        print(queue)
    return closest


class Test3Sum(unittest.TestCase):

    def test_0213_1(self):
        self.assertEqual(closest_3sum([0, 2, 1, -3], 1), 0)

    # def test_1214_1(self):
    #     self.assertEqual(closest_3sum([-1, 2, 1, -4], 1), 2)
    #
    # def test_long(self):
    #     self.assertEqual(closest_3sum([-1, 2, 1, -4, 8, 4, 6, 10, 3], 12), 13)
    #
    # def test_111_3(self):
    #     self.assertEqual(closest_3sum([1, 1, 1], 3), 3)
    #
    # def test_111_4(self):
    #     self.assertEqual(closest_3sum([1, 1, 2], 3), 4)
    #
    # def test_11_4(self):
    #     self.assertEqual(closest_3sum([1, 1], 3), 2)


if __name__ == "__main__":
    unittest.main()
