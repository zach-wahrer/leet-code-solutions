import unittest


# Iterative O(n)? time, O(1) space solution
def is_happy_iter(n: int) -> bool:

    while True:
        if n == 1:
            return True
        elif n == 4:
            return False

        new_number = 0
        for i in str(n)[::]:
            new_number += int(i) ** 2
        n = new_number


# Recursive solution
def is_happy(n: int) -> bool:

    def _happy(n):
        if n == 1:
            return True
        elif n == 4:
            return False

        new_number = 0
        for i in str(n)[::]:
            new_number += int(i) ** 2

        return _happy(new_number)

    return _happy(n)


class TestIsHappy(unittest.TestCase):

    def test_19(self):
        self.assertTrue(is_happy(19))

    def test_1(self):
        self.assertTrue(is_happy(1))

    def test_15(self):
        self.assertFalse(is_happy(15))

    def test_4(self):
        self.assertFalse(is_happy(4))

    def test_150(self):
        self.assertFalse(is_happy(150))


if __name__ == "__main__":
    unittest.main()
