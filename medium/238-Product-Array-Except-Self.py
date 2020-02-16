import unittest


# O(n**2) time, O(1) space solution - Fails Time Limit, which was expected
# Iterate through the list, multiplying everything but i
# Put that value in an array
# Return array
def product_array_except_self_naive(nums: list) -> list:
    if len(nums) == 1:
        return [0]
    output = []

    for i, not_product_num in enumerate(nums):
        product = 1
        for num in nums[:i]:
            product *= num
        for num in nums[i + 1:]:
            product *= num
        output.append(product)

    return output


# O(n) time and space solution
def product_array_except_self(nums: list) -> list:
    if len(nums) == 1:
        return [0]

    answers, left, right = [], [1], [1]
    product = 1
    for i in nums[:len(nums) - 1]:
        left.append(i * product)
        product *= i

    product = 1
    for i in nums[::-1]:
        right.append(i * product)
        product *= i
    right.pop()
    right.reverse()

    for l, r in zip(right, left):
        answers.append(r * l)

    return answers


class TestProductArray(unittest.TestCase):
    def test_45182(self):
        input = product_array_except_self([4, 5, 1, 8, 2])
        self.assertEqual(input, [80, 64, 320, 40, 160])

    def test_1234(self):
        input = product_array_except_self([1, 2, 3, 4])
        self.assertEqual(input, [24, 12, 8, 6])

    def test_12(self):
        input = product_array_except_self([1, 2])
        self.assertEqual(input, [2, 1])

    def test_012(self):
        input = product_array_except_self([0, 1, 2])
        self.assertEqual(input, [2, 0, 0])

    def test_013(self):
        input = product_array_except_self([1, 2, 3])
        self.assertEqual(input, [6, 3, 2])

    def test_1(self):
        input = product_array_except_self([1])
        self.assertEqual(input, [0])

    def test_11(self):
        input = product_array_except_self([1, 1])
        self.assertEqual(input, [1, 1])


if __name__ == "__main__":
    unittest.main()
