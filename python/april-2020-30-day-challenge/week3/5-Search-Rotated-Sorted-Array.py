import unittest


# O(log n) binary search solution
def search_rotated(nums: list, target: int):
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle

        if nums[start] <= nums[middle]:
            if nums[start] <= target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1

        else:
            if nums[end] >= target > nums[middle]:
                start = middle + 1
            else:
                end = middle - 1

    return -1


class TestSearch(unittest.TestCase):
    def test_513_3(self):
        self.assertEqual(search_rotated([5, 1, 3], 3), 2)

    def test_4567012_0(self):
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_4567012_3(self):
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_1_1(self):
        self.assertEqual(search_rotated([1], 1), 0)

    def test_13_1(self):
        self.assertEqual(search_rotated([1, 3], 3), 1)

    def test_351_3(self):
        self.assertEqual(search_rotated([3, 5, 1], 3), 0)


if __name__ == "__main__":
    unittest.main()
