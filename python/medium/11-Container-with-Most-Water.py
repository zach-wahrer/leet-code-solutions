import unittest


# Two pointer solution
def most_water(height: list) -> int:
    left = 0
    right = len(height) - 1
    max_water = []

    while left != right:
        max_for_section = min(height[left], height[right])
        max_water.append(max_for_section * (right - left))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max(max_water)


class TestMostWater(unittest.TestCase):

    def test_186254937_49(self):
        self.assertEqual(most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_11_1(self):
        self.assertEqual(most_water([1, 1]), 1)

    def test_80_0(self):
        self.assertEqual(most_water([8, 0]), 0)

    def test_810_1(self):
        self.assertEqual(most_water([8, 1, 0]), 1)


if __name__ == "__main__":
    unittest.main()
