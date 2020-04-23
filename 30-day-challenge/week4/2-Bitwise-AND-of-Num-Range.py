import unittest


def get_and_range(m: int, n: int) -> int:
    pass


class TestBitwiseANDRange(unittest.TestCase):
    def test_5_7(self):
        self.assertEqual(get_and_range(5, 7), 4)

    def test_0_1(self):
        self.assertEqual(get_and_range(0, 1), 0)


if __name__ == "__main__":
    unittest.main()
