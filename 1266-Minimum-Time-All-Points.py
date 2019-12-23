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


def min_time(points):
    sec = 0
    for i in range(0, len(points)):
        cur = points[i]
        # Check for next coordinate
        if i < len(points) - 1:
            next = points[i + 1]
        else:
            break

        while True:
            # Check to see if we need to keep going
            if cur[0] == next[0] and cur[1] == next[1]:
                break
            # If next x coord is higher
            if cur[0] < next[0]:
                cur[0] += 1
                sec += 1
                if cur[1] < next[1]:
                    cur[1] += 1
                elif cur[1] > next[1]:
                    cur[1] -= 1
            # If next x coord is lower
            elif cur[0] > next[0]:
                cur[0] -= 1
                sec += 1
                if cur[1] < next[1]:
                    cur[1] += 1
                elif cur[1] > next[1]:
                    cur[1] -= 1
            # Get y coord to be equal
            else:
                if cur[1] < next[1]:
                    cur[1] += 1
                    sec += 1
                elif cur[1] > next[1]:
                    cur[1] -= 1
                    sec += 1
    return sec


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
