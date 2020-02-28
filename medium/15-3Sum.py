import unittest


# Dict / math solution - passes LeetCode (just differing order on my tests)
def three_sum(nums: list) -> list:

    def gen_solution(items: list) -> tuple:
        items.sort()
        return tuple(items)

    pos_nums = {}
    neg_nums = {}
    zero_count = 0

    solutions = set()

    for i in nums:
        if i == 0:
            zero_count += 1
        elif i > 0:
            if i in pos_nums:
                pos_nums[i] += 1
            else:
                pos_nums[i] = 1
        else:
            if i in neg_nums:
                neg_nums[i] += 1
            else:
                neg_nums[i] = 1

    for num in set(nums):
        if num < 0:
            for pos in pos_nums:
                sol_num = -(num + pos)

                if sol_num in pos_nums:
                    if sol_num == pos and pos_nums[pos] - 1 < 1:
                        continue
                    else:
                        [num, pos, sol_num]
                        solutions.add(gen_solution([num, pos, sol_num]))
        elif num > 0:
            for neg in neg_nums:
                sol_num = -(num + neg)
                if sol_num in neg_nums:
                    if sol_num == neg and neg_nums[neg]-1 < 1:
                        continue
                    else:
                        solutions.add(gen_solution([num, neg, sol_num]))
                elif sol_num == 0 and zero_count > 0:
                    solutions.add(gen_solution([num, neg, 0]))

        elif zero_count >= 3:
            solutions.add(gen_solution([0, 0, 0]))

    solutions = [list(i) for i in solutions]

    return solutions


class TestThreeSum(unittest.TestCase):

    def test_101214(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])

    def test_zeros(self):
        self.assertEqual(three_sum([0, 0, 0, 1]), [[0, 0, 0]])

    def test_non_dupe(self):
        self.assertEqual(three_sum([3, 0, -2, -1, 1, 2]), [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])


if __name__ == "__main__":
    unittest.main()
