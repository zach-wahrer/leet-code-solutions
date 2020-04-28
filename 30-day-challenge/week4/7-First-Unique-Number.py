import unittest


# O(n) solution
class FirstUnique:
    from collections import OrderedDict

    def __init__(self, nums: list):
        self.queue = self.OrderedDict()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        for key in list(self.queue.keys()):
            if self.queue[key]:
                return key
        return -1

    def add(self, value: int) -> None:
        if value in self.queue:
            self.queue[value] = False
        else:
            self.queue[value] = True


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
