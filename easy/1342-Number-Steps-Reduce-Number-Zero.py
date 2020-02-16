import unittest


# Naive O(n) solution
def reduce_num_to_zero_naive(num: int) -> int:

    if num == "":
        return 0

    count = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        count += 1

    return count


# Recursive O(n) solution
def reduce_num_to_zero(num: int) -> int:

    if num == "":
        return 0

    count = 0

    def _reduce_num_to_zero(num, count):
        if num == 0:
            return count

        count += 1
        if num % 2 == 0:
            return _reduce_num_to_zero(num / 2, count)
        else:
            return _reduce_num_to_zero(num - 1, count)

    return _reduce_num_to_zero(num, count)


class TestReduceToZero(unittest.TestCase):

    def test_14(self):
        input = reduce_num_to_zero(14)
        self.assertEqual(input, 6)

    def test_8(self):
        input = reduce_num_to_zero(8)
        self.assertEqual(input, 4)

    def test_123(self):
        input = reduce_num_to_zero(123)
        self.assertEqual(input, 12)

    def test_blank(self):
        input = reduce_num_to_zero("")
        self.assertEqual(input, 0)

    def test_0(self):
        input = reduce_num_to_zero(0)
        self.assertEqual(input, 0)


if __name__ == "__main__":
    unittest.main()
