import unittest


def smaller_nums(nums: list) -> list:
    answer = []
    for index1, first_num in enumerate(nums):
        lower = 0
        for index2, second_num in enumerate(nums):
            if index1 != index2:
                if first_num > second_num:
                    lower += 1
        answer.append(lower)

    return answer


class TestSmallerNums(unittest.TestCase):

    def test_81223(self):
        self.assertEqual(smaller_nums([8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])

    def test_6548(self):
        self.assertEqual(smaller_nums([6, 5, 4, 8]), [2, 1, 0, 3])

    def test_7777(self):
        self.assertEqual(smaller_nums([7, 7, 7, 7]), [0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
