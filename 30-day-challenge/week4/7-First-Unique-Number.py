import unittest


# Times out on leetcode
class FirstUnique:
    from collections import Counter

    def __init__(self, nums: list):
        self.queue = nums

    def showFirstUnique(self) -> int:
        counts = self.Counter(self.queue)
        for num in self.queue:
            if counts[num] == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)


class TestFirstUnique(unittest.TestCase):
    def test_235(self):
        first_unique = FirstUnique([2, 3, 5])
        self.assertEqual(first_unique.showFirstUnique(), 2)
        first_unique.add(5)
        self.assertEqual(first_unique.showFirstUnique(), 2)
        first_unique.add(2)
        self.assertEqual(first_unique.showFirstUnique(), 3)
        first_unique.add(3)
        self.assertEqual(first_unique.showFirstUnique(), -1)


if __name__ == "__main__":
    unittest.main()
