import unittest


# Brute force recursive solution (times out on LeetCode, as expected)
def min_jumps_brute(nums: list) -> int:
    jumps_needed = set()

    def _min_jumps(remaining_list, jumps_completed):
        if len(remaining_list) == 1:
            jumps_needed.add(jumps_completed)
            return
        if len(remaining_list) - 1 <= remaining_list[0]:
            jumps_needed.add(jumps_completed + 1)
            return

        for i in range(1, remaining_list[0] + 1):
            _min_jumps(remaining_list[i:], jumps_completed + 1)

    _min_jumps(nums, 0)
    return min(jumps_needed)


# Brute Recursive Solution. Much faster, but still times out on LeetCode)
def min_jumps_brute_faster(nums: list) -> int:
    jumps_needed = set()

    def _min_jumps(remaining_list, jumps_completed):
        if jumps_needed and min(jumps_needed) < jumps_completed:
            return
        if len(remaining_list) == 1:
            jumps_needed.add(jumps_completed)
            return
        if len(remaining_list) - 1 <= remaining_list[0]:
            jumps_needed.add(jumps_completed + 1)
            return

        for i in range(1, remaining_list[0] + 1):
            _min_jumps(remaining_list[i:], jumps_completed + 1)

    _min_jumps(nums, 0)

    return min(jumps_needed)


# Iterative solution, but fails inobvious cases
def min_jumps(nums: list) -> int:

    position = 0
    jumps_taken = 0
    spaces_remaining_in_jump = nums[0]

    while position < len(nums):
        if position == len(nums) - 1:
            return jumps_taken

        possible_steps = nums[position]

        while possible_steps > 0:
            possible_steps -= 1
            if nums[possible_steps] > possible_steps:
                position += nums[possible_steps]
                skipped = True
                break

        if not skipped:
            position += nums[position]
        jumps_taken += 1

    return jumps_taken


class TestMinJumps(unittest.TestCase):

    def test_23114(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4]), 2)

    def test_1111(self):
        self.assertEqual(min_jumps([1, 1, 1, 1]), 3)

    def test_tricky(self):
        self.assertEqual(min_jumps([2, 8, 1, 1, 1, 1, 1, 1, 1, 1]), 2)

    def test_tricky2(self):
        self.assertEqual(min_jumps([2, 8, 2, 1, 2, 1, 3, 1, 1, 1]), 2)

    def test_short(self):
        self.assertEqual(min_jumps([1]), 0)

    def test_leet(self):
        self.assertEqual(min_jumps([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1,
                                    5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]), 5)


if __name__ == "__main__":
    unittest.main()
