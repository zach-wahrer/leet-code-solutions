import unittest


# O(n) time, O(1) space solution
def remove_dupes(nums: list) -> int:

    p1, p2 = 0, 0
    length_count = 1

    while p2 < len(nums) - 1:
        while nums[p1] == nums[p2]:
            if p2 < len(nums):
                p2 += 1
            if p2 == len(nums):
                break
        p1 += 1
        if p2 != len(nums):
            nums[p1] = nums[p2]
            length_count += 1

    return length_count


class TestRemovingDuplicates(unittest.TestCase):

    def test_0011122334(self):
        input_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        new_list_len = remove_dupes(input_list)
        self.assertEqual(new_list_len, 5)
        self.assertEqual(input_list, [0, 1, 2, 3, 4, 2, 2, 3, 3, 4])

    def test_0(self):
        input_list = [0]
        new_list_len = remove_dupes(input_list)
        self.assertEqual(new_list_len, 1)
        self.assertEqual(input_list, [0])

    def test_000123(self):
        input_list = [0, 0, 0, 1, 2, 3]
        new_list_len = remove_dupes(input_list)
        self.assertEqual(new_list_len, 4)
        self.assertEqual(input_list, [0, 1, 2, 3, 2, 3])

    def test_12(self):
        input_list = [1, 2]
        new_list_len = remove_dupes(input_list)
        self.assertEqual(new_list_len, 2)
        self.assertEqual(input_list, [1, 2])

    def test_11(self):
        input_list = [1, 1]
        new_list_len = remove_dupes(input_list)
        self.assertEqual(new_list_len, 1)
        self.assertEqual(input_list, [1, 1])


if __name__ == "__main__":
    unittest.main()
