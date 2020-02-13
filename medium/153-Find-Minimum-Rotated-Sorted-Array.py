import unittest


# Naive O(n) solution
def find_min_naive(nums: list) -> int:
    try:
        return min(nums)
    except ValueError:
        return None


# Two pointer O(n) solution
def find_min_two_pointer(nums: list) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    right = len(nums) - 1
    look_behind = right - 1
    while True:
        if nums[look_behind] > nums[right]:
            return nums[right]
        right -= 1
        look_behind -= 1


# Binary Search O(log n) solution
def find_min(nums: list) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    def get_middle(start: int, end: int) -> int:
        return (start + end) // 2

    start = 0
    end = len(nums) - 1
    middle = get_middle(start, end)

    while True:
        if start > end:
            return nums[0]

        if nums[middle - 1] > nums[middle]:
            return nums[middle]
        if middle < len(nums) - 1:
            if nums[middle + 1] < nums[middle]:
                return nums[middle + 1]
        else:
            return nums[0]

        if nums[middle] > nums[start]:
            start = middle + 1
            middle = get_middle(start, end)
        else:
            end = middle - 1
            middle = get_middle(start, end)


class TestMinimumRotatedSortedArray(unittest.TestCase):

    def test_34512(self):
        input = find_min([3, 4, 5, 1, 2])
        self.assertEqual(input, 1)

    def test_4567012(self):
        input = find_min([4, 5, 6, 7, 0, 1, 2])
        self.assertEqual(input, 0)

    def test_123(self):
        input = find_min([1, 2, 3])
        self.assertEqual(input, 1)

    def test_12345(self):
        input = find_min([1, 2, 3, 4, 5])
        self.assertEqual(input, 1)

    def test_890123456(self):
        input = find_min([8, 9, 0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(input, 0)

    def test_12345210(self):
        input = find_min([1, 2, 3, 4, 5, -2, -1, 0])
        self.assertEqual(input, -2)

    def test_99100567(self):
        input = find_min([99, 100, 5, 6, 7])
        self.assertEqual(input, 5)

    def test_blank(self):
        input = find_min([])
        self.assertEqual(input, None)

    def test_two_items(self):
        input = find_min([2, 1])
        self.assertEqual(input, 1)

    def test_one_item(self):
        input = find_min([100])
        self.assertEqual(input, 100)

    def test_three_items(self):
        input = find_min([100, 101, 99])
        self.assertEqual(input, 99)


if __name__ == "__main__":
    unittest.main()
