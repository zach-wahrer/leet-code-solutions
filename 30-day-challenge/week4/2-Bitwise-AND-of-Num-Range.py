import unittest


def get_and_range(m: int, n: int) -> int:
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1
    return n << i


class TestBitwiseANDRange(unittest.TestCase):
    def test_5_7(self):
        self.assertEqual(get_and_range(5, 7), 4)

    def test_0_1(self):
        self.assertEqual(get_and_range(0, 1), 0)


if __name__ == "__main__":
    unittest.main()
