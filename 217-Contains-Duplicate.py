'''
Psudocode:
    Loop through list elments
        Check if element is in list more than once
'''

import unittest


def contains_duplicate(nums: list) -> bool:
    for i in nums:
        if nums.count(i) > 1:
            return True
    return False


class TestDuplicate(unittest.TestCase):
    def test_1231(self):
        input = contains_duplicate([1, 2, 3, 1])
        output = True
        self.assertEqual(input, output)

    def test_1234(self):
        input = contains_duplicate([1, 2, 3, 4])
        output = False
        self.assertEqual(input, output)

    def test_1113343242(self):
        input = contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        output = True
        self.assertEqual(input, output)

    def test_minus12344(self):
        input = contains_duplicate([-1, -2, -3, -4, -4])
        output = True
        self.assertEqual(input, output)

    def test_001(self):
        input = contains_duplicate([0, 0, 1])
        output = True
        self.assertEqual(input, output)

    def test_01511(self):
        input = contains_duplicate([0, 1, 5, 11])
        output = False
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
