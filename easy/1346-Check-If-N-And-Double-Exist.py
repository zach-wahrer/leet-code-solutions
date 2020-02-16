import unittest


# Naive O(n**2) solution
def check_double_of_n_naive(arr: list) -> bool:
    if arr.count(0) > 1:
        return True

    for i in arr:
        if 2 * i in arr and i != 0:
            return True
    return False


# Hash map O(n) time and space solution
def check_double_of_n(arr: list) -> bool:
    if arr.count(0) > 1:
        return True

    nums_set = set(arr)
    for i in arr:
        if 2 * i in nums_set and i != 0:
            return True
    return False


class TestDoubleN(unittest.TestCase):
    def test_00(self):
        input = check_double_of_n([0, 0])
        self.assertTrue(input)

    def test_201019468(self):
        input = check_double_of_n([-2, 0, 10, -19, 4, 6, -8])
        self.assertFalse(input)

    def test_10253(self):
        input = check_double_of_n([10, 2, 5, 3])
        self.assertTrue(input)

    def test_711411(self):
        input = check_double_of_n([7, 1, 14, 11])
        self.assertTrue(input)

    def test_3171(self):
        input = check_double_of_n([3, 1, 7, 11])
        self.assertFalse(input)

    def test_82(self):
        input = check_double_of_n([8, 2])
        self.assertFalse(input)

    def test_12(self):
        input = check_double_of_n([1, 2])
        self.assertTrue(input)


if __name__ == "__main__":
    unittest.main()
