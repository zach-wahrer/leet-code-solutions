import unittest


# Iterative O(n)? time, O(1) space solution
def is_happy(n: int) -> bool:

    while True:
        if n == 1:
            return True
        if n == 4:
            return False

        acc = 0
        for i in str(n)[::]:
            acc += int(i) ** 2
        n = acc


class TestHappyNumber(unittest.TestCase):
    def test_19(self):
        self.assertTrue(is_happy(19))

    def test_4(self):
        self.assertFalse(is_happy(4))

    def test_1(self):
        self.assertTrue(is_happy(1))


if __name__ == "__main__":
    unittest.main()
