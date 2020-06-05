import unittest


# O(1) solution
class FirstUnique:

    def __init__(self, nums: list):
        self.nums_seen = set()
        self.unique_nums = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        for key in self.unique_nums.keys():
            return key
        return -1

    def add(self, value: int) -> None:
        if value not in self.nums_seen:
            self.nums_seen.add(value)
            self.unique_nums[value] = True
        elif value in self.unique_nums:
            del self.unique_nums[value]


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

    def test_777777(self):
        first_unique = FirstUnique([7, 7, 7, 7, 7, 7])
        self.assertEqual(first_unique.showFirstUnique(), -1)
        first_unique.add(7)
        first_unique.add(3)
        first_unique.add(3)
        first_unique.add(7)
        first_unique.add(17)
        first_unique.add(18)
        self.assertEqual(first_unique.showFirstUnique(), 17)


if __name__ == "__main__":
    unittest.main()
