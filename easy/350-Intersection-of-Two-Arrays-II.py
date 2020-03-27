import unittest


def array_intersection(nums1: list, nums2: list) -> list:
    pass


class TestArrayIntersection(unittest.TestCase):

    def test_1221_22(self):
        input = array_intersection([1, 2, 2, 1], [2, 2])
        self.assertEqual(input, [2, 2])

    def test_495_94984(self):
        input = array_intersection([4, 9, 5], [9, 4, 9, 8, 4])
        self.assertEqual(input, [4, 9])


if __name__ == "__main__":
    unittest.main()
