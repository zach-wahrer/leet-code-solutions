import unittest


# O(log n) time, O(1) space
# Doesn't work correctly
def binary_search_invalid(nums: list, target: int) -> int:
    start = 0
    finish = len(nums) - 1
    middle = int(finish / 2)

    if finish == 0:
        if nums[0] == target:
            return 0
        return -1

    end_check = 0
    while True:
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
            middle = start + (finish - start) // 2
        else:
            middle = start + (middle - 1) // 2
        if end_check == middle:
            return -1
        end_check = middle


# O(log n) time, O(1) space
def binary_search_logn(nums: list, target: int) -> int:
    start = 0
    end = len(nums) - 1
    middle = end // 2
    end_check = None

    while True:
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
            middle = start + (end - start) // 2
        else:
            end = middle - 1
            middle = start + (end - start) // 2
        if end_check == middle:
            return -1
        end_check = middle


# O(n) time, O(1) space
def binary_search(nums: list, target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1


class TestBinarySearch(unittest.TestCase):

    def test_list_value_found_end(self):
        input = binary_search([-1, 0, 3, 5, 9, 12], 9)
        self.assertEqual(input, 4)

    def test_list_value_found_last(self):
        input = binary_search([-1, 0, 3, 5, 9, 12, 13], 13)
        self.assertEqual(input, 6)

    def test_list_value_found_beginning(self):
        input = binary_search([-1, 0, 3, 5, 9, 12], 0)
        self.assertEqual(input, 1)

    def test_list_value_not_found(self):
        input = binary_search([-1, 0, 3, 5, 9, 12], 2)
        self.assertEqual(input, -1)

    def test_short_list_value_found(self):
        input = binary_search([999, 1000], 1000)
        self.assertEqual(input, 1)

    def test_short_list_value_not_found(self):
        input = binary_search([999, 1000], 888)
        self.assertEqual(input, -1)

    def test_one_list_value_not_found(self):
        input = binary_search([1], 2)
        self.assertEqual(input, -1)

    def test_one_list_value_found(self):
        input = binary_search([1], 1)
        self.assertEqual(input, 0)

    def test_three_list_value_found(self):
        input = binary_search([1, 2, 3], 3)
        self.assertEqual(input, 2)


if __name__ == "__main__":
    unittest.main()
