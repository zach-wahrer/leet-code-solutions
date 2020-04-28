import unittest


# O(n) solution, passes, but seems slow
class FirstUnique:
    from collections import OrderedDict

    def __init__(self, nums: list):
        self.uniques = self.OrderedDict()
        self.queue = []
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        keys = list(self.uniques.keys())

        if self.uniques[keys[0]]:
            return keys[0]
        elif self.uniques[keys[-1]]:
            return keys[-1]
        else:
            return -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        if value in self.uniques:
            self.uniques[value] = False
            self.uniques.move_to_end(value)
        else:
            self.uniques[value] = True


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
        print(first_unique.queue)
        print(first_unique.uniques)
        self.assertEqual(first_unique.showFirstUnique(), 17)


if __name__ == "__main__":
    unittest.main()
