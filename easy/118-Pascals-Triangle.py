import unittest


def gen_pascals(numRows: int) -> list:
    pass


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
