"""
Psudocode:
    Check if second coordinate is higher or lower than first
    If higher/lower
        Add/subtract 1 each side, incrementing counter, until one side is equal
        Add/subtract 1 remaining side, incrementing counter, until it is equal
        Repeat with next coordinate, starting from current posistion

    V2
    Check x,y are equal
    If neither, add or subtract 1 as needed
            Increment counter by 1 if both values change
    If one is equal,
        Add or subtract 1 from the other coordinate
            Increment counter by 1
    Repeat until values are equal
"""

import unittest


def distance_between_points(point1, point2):
    x_dif = abs(point1[0] - point2[0])
    y_dif = abs(point1[1] - point2[1])
    return max(x_dif, y_dif)


def min_time(points) -> int:
    sec = 0
    for current_point, next_point in zip(points[:-1], points[1:]):
        sec += distance_between_points(current_point, next_point)
    return sec


# Dan's one liner
def min_time2(points):
    return sum([max(abs(cp[0] - np[0]), abs(cp[1] - np[1])) for cp, np in zip(points[:-1], points[1:])])


class TestMinimum(unittest.TestCase):

    def test_113410(self):
        input = min_time([[1, 1], [3, 4], [-1, 0]])
        output = 7
        self.assertEqual(input, output)

    def test_3222(self):
        input = min_time([[3, 2], [-2, 2]])
        output = 5
        self.assertEqual(input, output)

    def test_005500(self):
        input = min_time([[0, 0], [5, 5], [0, 0]])
        output = 10
        self.assertEqual(input, output)

    def test_119600(self):
        input = min_time([[1, 1], [9, 6], [0, 0]])
        output = 17
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
