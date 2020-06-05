import unittest


# O(n**2) time solution
def product_except_self_slow(nums: list) -> list:
    output = []
    for _ in range(len(nums)):
        output.append(1)
    for index, number in enumerate(nums):
        for pos, num in enumerate(output):
            if index != pos:
                output[pos] *= number
    return output


# O(n) solution
def product_except_self(nums: list) -> list:
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


class TestProducts(unittest.TestCase):
    def test_1234(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_12(self):
        self.assertEqual(product_except_self([1, 2]), [2, 1])


if __name__ == "__main__":
    unittest.main()
