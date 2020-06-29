import unittest


def twoSum(numbers: list, target: int) -> list:
    pass


class TestTwoSum(unittest.TestCase):

    def test_twoSum_short_input(self):
        got = twoSum([1, 2, 3], 5)
        want = [2, 3]
        self.assertEqual(got, want)

    def test_twoSum_medium_input(self):
        got = twoSum([2, 7, 11, 15], 9)
        want = [1, 2]
        self.assertEqual(got, want)

    def test_twoSum_long_input(self):
        got = twoSum([2, 7, 11, 15, 8, 16, 9, 99, 1], 100)
        want = [8, 9]
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
