import unittest


# O(n*m) time/space solution
def array_intersection(nums1: list, nums2: list) -> list:
    from collections import Counter

    count1 = Counter(nums1)
    count2 = Counter(nums2)
    output = []

    for i in count1:
        if count2[i]:
            for _ in range(min(count1[i], count2[i])):
                output.append(i)

    return output


class TestArrayIntersection(unittest.TestCase):

    def test_1221_22(self):
        input = array_intersection([1, 2, 2, 1], [2, 2])
        self.assertEqual(input, [2, 2])

    def test_495_94984(self):
        input = array_intersection([4, 9, 5], [9, 4, 9, 8, 4])
        self.assertEqual(input, [4, 9])

    def test_blank(self):
        input = array_intersection([], [])
        self.assertEqual(input, [])

    def test_single_val_match(self):
        input = array_intersection([1], [1])
        self.assertEqual(input, [1])

    def test_single_val_no_match(self):
        input = array_intersection([1], [2])
        self.assertEqual(input, [])


if __name__ == "__main__":
    unittest.main()
