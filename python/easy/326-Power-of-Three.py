import unittest


# Iterative O(n) time / O(1) space solution
def is_power_three_iter(n: int) -> bool:
    if n == 1:
        return True
    accumulator = 3
    while accumulator <= n:
        if accumulator == n:
            return True
        accumulator *= 3
    return False


# Recursive O(n) time solution
def is_power_three(n: int) -> bool:
    if n == 1:
        return True

    def _find_power(number):
        if number == 3:
            return True
        if number < 3:
            return False

        return _find_power(number / 3)

    return _find_power(n)


class TestPowerOfThree(unittest.TestCase):

    def test_1(self):
        self.assertTrue(is_power_three(1))

    def test_27(self):
        self.assertTrue(is_power_three(27))

    def test_9(self):
        self.assertTrue(is_power_three(9))

    def test_0(self):
        self.assertFalse(is_power_three(0))

    def test_45(self):
        self.assertFalse(is_power_three(45))


if __name__ == "__main__":
    unittest.main()
