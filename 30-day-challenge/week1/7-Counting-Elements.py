import unittest


# O(n log n) time / O(1) space solution
def count_elements_sorting(arr: list) -> int:
    arr.sort()
    total_count, provisional_count = 0, 1
    p1, p2 = 0, 1

    while p2 < len(arr):
        while p2 < len(arr) and arr[p1] == arr[p2]:
            provisional_count += 1
            p2 += 1
        if p2 < len(arr) and arr[p1] + 1 == arr[p2]:
            if provisional_count > 1:
                total_count += provisional_count
                provisional_count = 1
            else:
                total_count += 1

        provisional_count = 1
        p1 = p2
        p2 += 1

    return total_count


# O(n) time/space solution
def count_elements(arr: list) -> int:
    from collections import Counter
    counts = Counter(arr)
    total_count = 0

    for number in counts:
        if number + 1 in counts:
            total_count += counts[number]

    return total_count


class TestCounts(unittest.TestCase):
    def test_leet2(self):
        self.assertEqual(count_elements([0, 6, 3, 4, 2, 10, 4, 3, 10, 0]), 3)

    def test_leet(self):
        self.assertEqual(count_elements([2, 9, 0, 7, 6, 2, 7, 7, 0]), 1)

    def test_short(self):
        self.assertEqual(count_elements([1, 2, 3]), 2)

    def test_long(self):
        self.assertEqual(count_elements([1, 1, 3, 3, 5, 5, 7, 7]), 0)

    def test_medium(self):
        self.assertEqual(count_elements([1, 3, 2, 3, 5, 0]), 3)

    def test_duplicates(self):
        self.assertEqual(count_elements([1, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
