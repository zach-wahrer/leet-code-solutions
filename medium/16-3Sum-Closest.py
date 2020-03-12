import unittest


def closest_3sum(nums: list, target: int) -> int:
    pass


class Test3Sum(unittest.TestCase):

    def test_1214_1(self):
        self.assertEqual(closest_3sum([-1, 2, 1, -4], 1), 2)

    def test_111_3(self):
        self.assertEqual(closest_3sum([1, 1, 1], 3), 3)

    def test_111_4(self):
        self.assertEqual(closest_3sum([1, 1, 2], 3), 4)


if __name__ == "__main__":
    unittest.main()
