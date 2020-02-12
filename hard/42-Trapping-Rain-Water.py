'''
Psudocode:

'''

import unittest

"""
def how_much_can_city_hold(city: list) -> int:
    water = 0
    for i, building in enumerate(city):
        if i > 0 and i+1 < len(city):
            left_tallest = max(city[:i])
            right_tallest = max(city[i+1:])
            max_capacity = min(left_tallest, right_tallest)
            water += max(0, max_capacity - building)
    return water
"""


def how_much_can_city_hold(city: list) -> int:
    water = 0
    left = 0
    right = len(city) - 1
    left_max = 0
    right_max = 0
    if city == []:
        return 0
    while left != right:
        left_max = max(city[left], left_max)
        right_max = max(city[right], right_max)
        max_capacity = min(left_max, right_max)
        if city[left] < city[right]:
            water += max(0, max_capacity - city[left])
            left += 1
        else:
            water += max(0, max_capacity - city[right])
            right -= 1

    return water


class TestHowMuchCanHold(unittest.TestCase):

    def test_10535(self):
        input = how_much_can_city_hold([1, 0, 5, 3, 5])
        output = 3
        self.assertEqual(input, output)

    def test_010(self):
        input = how_much_can_city_hold([0, 1, 0])
        output = 0
        self.assertEqual(input, output)

    def test_102(self):
        input = how_much_can_city_hold([1, 0, 2])
        output = 1
        self.assertEqual(input, output)

    def test_1001(self):
        input = how_much_can_city_hold([1, 0, 0, 1])
        output = 2
        self.assertEqual(input, output)

    def test_blank(self):
        input = how_much_can_city_hold([])
        output = 0
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
