import unittest


class FirstUnique:

    def __init__(self, nums: list):
        pass

    def showFirstUnique(self) -> int:
        pass

    def add(self, value: int) -> None:
        pass


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
