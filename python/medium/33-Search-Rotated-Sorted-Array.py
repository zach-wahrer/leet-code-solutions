import unittest


# Naive solution O(n) time, O(1) space
def search_pos_rotated_array_naive(nums: list, target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1


# Doesn't work - Recursive Binary Search solution O(log n) time, O(1) space
def valid_edge_case(nums, target):
    if not nums:
        return (True, -1)

    if len(nums) == 1:
        if nums[0] == target:
            return (True, 0)
        else:
            return (True, -1)

    if nums[-2] == target:
        return (True, len(nums) - 2)
    if nums[1] == target:
        return (True, 1)

    return (False, None)


def finished_searching(start, middle, end, nums, target):
    if start > end or middle == len(nums) - 1:
        return (True, -1)
    if nums[start] == target:
        return (True, start)
    if nums[end] == target:
        return (True, end)
    if nums[middle] == target:
        return (True, middle)
    if nums[middle + 1] == target:
        return (True, middle + 1)
    if nums[middle - 1] == target:
        return (True, middle - 1)

    return (False, None)


def get_middle(start, end):
    return (start + end) // 2


def search_pos_rotated_array_recursive(nums: list, target: int) -> int:

    finished, pointer = valid_edge_case(nums, target)
    if finished:
        return pointer

    def _search_pos_rotated_array(start, end):
        segment_rotated = nums[start] > nums[end]
        middle = get_middle(start, end)

        finished, pointer = finished_searching(start, middle, end,
                                               nums, target)
        if finished:
            return pointer
        print(nums[start], nums[middle], nums[end], segment_rotated)
        if segment_rotated:
            if target <= nums[end] or target > nums[middle]:
                return _search_pos_rotated_array(middle + 1, end)
            else:
                return _search_pos_rotated_array(start, middle - 1)

        else:
            if target > nums[middle]:
                return _search_pos_rotated_array(middle + 1, end)
            else:
                return _search_pos_rotated_array(start, middle - 1)

    return _search_pos_rotated_array(0, len(nums) - 1)


# Binary Search solution O(log n) time, O(1) space
def search_pos_rotated_array_loop(nums: list, target: int) -> int:
    if not nums:
        return -1

    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    if nums[-2] == target:
        return len(nums) - 2
    if nums[1] == target:
        return 1

    def get_middle(start, end):
        return (start + end) // 2

    start = 0
    end = len(nums) - 1
    list_rotated = nums[start] > nums[end]

    while True:
        middle = get_middle(start, end)
        print(start, middle, end)
        if start > end or middle == len(nums) - 1:
            return -1

        if nums[middle] == target:
            return middle
        if nums[middle + 1] == target:
            return middle + 1
        if nums[middle - 1] == target:
            return middle - 1

        if not list_rotated:
            if target > nums[middle]:
                start = middle + 1
            else:
                end = middle - 1

        else:
            if target <= nums[end]:
                start = middle + 1
            else:
                end = middle - 1


# Binary Search - O(log n) time, O(1) space
def search_pos_rotated_array(nums: list, target: int) -> int:
    start = 0
    finish = len(nums) - 1

    while start <= finish:
        mid = (start + finish) // 2
        if nums[mid] == target:
            return mid
        elif nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                finish = mid - 1
            else:
                start = mid + 1
        else:
            if nums[finish] >= target > nums[mid]:
                start = mid + 1
            else:
                finish = mid - 1

    return -1


class SearchRotatedSortedArray(unittest.TestCase):

    def test_456789123_1(self):
        input = search_pos_rotated_array([4, 5, 6, 7, 8, 9, 1, 2, 3], 1)
        self.assertEqual(input, 6)

    def test_long(self):
        input = search_pos_rotated_array([266, 267, 268, 269, 271, 278, 282, 292, 293, 298, 6, 9, 15, 19, 21, 26, 33, 35, 37, 38, 39, 46, 49, 54, 65, 71, 74, 77, 79, 82, 83, 88, 92, 93, 94, 97, 104, 108, 114, 115, 117, 122,
                                          123, 127, 128, 129, 134, 137, 141, 142, 144, 147, 150, 154, 160, 163, 166, 169, 172, 173, 177, 180, 183, 184, 188, 198, 203, 208, 210, 214, 218, 220, 223, 224, 233, 236, 241, 243, 253, 256, 257, 262, 263], 208)
        self.assertEqual(input, 67)

    def test_long2(self):
        input = search_pos_rotated_array([113, 114, 115, 116, 117, 118, 123, 124, 127, 129, 130, 133, 134, 142, 143, 147, 148, 149, 150, 151, 152, 154, 155, 158, 159, 160, 161, 164, 165, 166, 174, 175, 177, 178, 179, 180, 181, 183, 185, 187, 190, 192, 193, 194, 196, 199, 200, 201, 203, 205, 206, 207, 208, 209, 210, 215, 216, 218, 220, 221, 223, 224, 228, 230, 231, 235, 236, 242,
                                          245, 247, 250, 251, 257, 259, 261, 262, 263, 264, 265, 269, 271, 273, 277, 279, 280, 281, 282, 283, 285, 286, 288,    290, 293, 295, 296, 297, 0, 2, 4, 8, 9, 10, 11, 12, 15, 17, 20, 21, 22, 23, 24, 27, 29, 33, 35, 36, 37, 39, 43, 45, 48, 49, 52, 54, 55, 60, 64, 67, 68, 72, 73, 75, 76, 79, 85, 87, 88, 91, 94, 97, 99, 100, 101, 102, 103, 104, 105, 107, 108, 110, 112], 296)
        self.assertEqual(input, 94)

    def test_blank_5_found(self):
        input = search_pos_rotated_array([], 5)
        self.assertEqual(input, -1)

    def test_234567891_9_found(self):
        input = search_pos_rotated_array([2, 3, 4, 5, 6, 7, 8, 9, 1], 9)
        self.assertEqual(input, 7)

    def test_912345678_1_found(self):
        input = search_pos_rotated_array([9, 1, 2, 3, 4, 5, 6, 7, 8], 1)
        self.assertEqual(input, 1)

    def test_12345_5_found(self):
        input = search_pos_rotated_array([1, 2, 3, 4, 5], 5)
        self.assertEqual(input, 4)

    def test_123456_1_found(self):
        input = search_pos_rotated_array([1, 2, 3, 4, 5, 6], 1)
        self.assertEqual(input, 0)

    def test_4567012_6_found(self):
        input = search_pos_rotated_array([4, 5, 6, 7, 0, 1, 2], 2)
        self.assertEqual(input, 6)

    def test_4567012_1_found(self):
        input = search_pos_rotated_array([4, 5, 6, 7, 0, 1, 2], 1)
        self.assertEqual(input, 5)

    def test_4567012_4_found(self):
        input = search_pos_rotated_array([4, 5, 6, 7, 0, 1, 2], 4)
        self.assertEqual(input, 0)

    def test_4567012_3_not_found(self):
        input = search_pos_rotated_array([4, 5, 6, 7, 0, 1, 2], 3)
        self.assertEqual(input, -1)

    def test_len_1_found(self):
        input = search_pos_rotated_array([1], 1)
        self.assertEqual(input, 0)

    def test_len_1_not_found(self):
        input = search_pos_rotated_array([1], 2)
        self.assertEqual(input, -1)

    def test_len_2_found(self):
        input = search_pos_rotated_array([2, 1], 1)
        self.assertEqual(input, 1)

    def test_len_2_not_found(self):
        input = search_pos_rotated_array([2, 1], 0)
        self.assertEqual(input, -1)

    def test_123_1_found(self):
        input = search_pos_rotated_array([1, 2, 3], 1)
        self.assertEqual(input, 0)

    def test_123_4_not_found(self):
        input = search_pos_rotated_array([1, 2, 3], 4)
        self.assertEqual(input, -1)

    def test_12310_1_found(self):
        input = search_pos_rotated_array([1, 2, 3, -1, 0], -1)
        self.assertEqual(input, 3)

    def test_12310_2_found(self):
        input = search_pos_rotated_array([1, 2, 3, -1, 0], 2)
        self.assertEqual(input, 1)

    def test_45678123_6_found(self):
        input = search_pos_rotated_array([4, 5, 6, 7, 8, 1, 2, 3], 6)
        self.assertEqual(input, 2)

    def test_45678123_9_not_found(self):
        input = search_pos_rotated_array([4, 5, 6, 7, 8, 1, 2, 3], 9)
        self.assertEqual(input, -1)


if __name__ == "__main__":
    unittest.main()
