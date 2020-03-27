import unittest


# O(n) time/space solution
def gen_pascals(numRows: int) -> list:
    triangle = []

    def _gen_row(row_number, target_rows, triangle):
        if row_number > target_rows:
            return triangle

        if row_number == 1:
            triangle.append([1])
        elif row_number == 2:
            triangle.append([1, 1])
        else:
            pos = 0
            row = [1]
            for i in range(len(triangle[-1]) - 1):
                row.append(triangle[-1][pos] + triangle[-1][pos + 1])
                pos += 1
            row.append(1)
            triangle.append(row)

        return _gen_row(row_number + 1, target_rows, triangle)

    return _gen_row(1, numRows, triangle)


class TestGenPascals(unittest.TestCase):

    def test_5(self):
        triangle = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]

        ]
        self.assertEqual(gen_pascals(5), triangle)

    def test_1(self):
        triangle = [
            [1]
        ]
        self.assertEqual(gen_pascals(1), triangle)

    def test_2(self):
        triangle = [
            [1],
            [1, 1]
        ]
        self.assertEqual(gen_pascals(2), triangle)

    def test_3(self):
        triangle = [
            [1],
            [1, 1],
            [1, 2, 1]
        ]
        self.assertEqual(gen_pascals(3), triangle)


if __name__ == "__main__":
    unittest.main()
