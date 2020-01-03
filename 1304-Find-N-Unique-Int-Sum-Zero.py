'''
Psudocode:

'''

import unittest


def unique_ints(numbers: int) -> list:
    return 1


class TestUniqueList(unittest.TestCase):

    def test_5(self):
        input = unique_ints(5)
        possibles = [
            [-7, -1, 1, 3, 4],
            [-5, -1, 1, 2, 3],
            [-3, -1, 2, -2, 4]
        ]
        for output in possibles:
            if input == output:
                self.assertEqual(input, output)
                break
            if output == possibles[(len(possibles) - 1)]:
                self.assertEqual(input, possibles[(len(possibles) - 1)])

    def test_3(self):
        input = unique_ints(3)
        output = [-1, 0, 1]
        self.assertEqual(input, output)

    def test_1(self):
        input = unique_ints(1)
        output = [0]
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
