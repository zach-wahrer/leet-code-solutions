import unittest


# O(logn) time, O(1) space solution
def search_range(nums: list, target: int) -> list:
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return find_boundaries(middle, target, nums)
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1

    return [-1, -1]

def find_boundaries(index: int, target: int, nums: list) -> list:
    left_boundary = right_boundary = index

    while left_boundary > 0 and nums[left_boundary - 1] == target:
        left_boundary -= 1

    while right_boundary < len(nums) - 1 and nums[right_boundary + 1] == target:
        right_boundary += 1

    return [left_boundary, right_boundary]

class TestSearchRange(unittest.TestCase):
    def test_found(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertEqual(search_range(nums, target), [3, 4])

    def test_not_found(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        self.assertEqual(search_range(nums, target), [-1, -1])

    def test_blank(self):
        nums = []
        target = 6
        self.assertEqual(search_range(nums, target), [-1, -1])

    def test_1_element_input_found(self):
        nums = [1]
        target = 1
        self.assertEqual(search_range(nums, target), [0, 0])

    def test_1_element_input_not_found(self):
        nums = [1]
        target = 3
        self.assertEqual(search_range(nums, target), [-1, -1])

    def test_2_element_input_found(self):
        nums = [2, 2]
        target = 2
        self.assertEqual(search_range(nums, target), [0, 1])

    def test_2_element_input_not_found(self):
        nums = [2, 2]
        target = 4
        self.assertEqual(search_range(nums, target), [-1, -1])

if __name__ == "__main__":
    unittest.main()
