'''
Psudocode:

'''

import unittest


def search_input_pos(nums: list, target: int) -> int:
    pass


class TestPosistion(unittest.TestCase):

    def test_1356_5(self):
        input = search_input_pos([1, 3, 5, 6], 5)
        output = 2
        self.assertEqual(input, output)

    def test_1356_2(self):
        input = search_input_pos([1, 3, 5, 6], 2)
        output = 1
        self.assertEqual(input, output)

    def test_1356_7(self):
        input = search_input_pos([1, 3, 5, 6], 7)
        output = 4
        self.assertEqual(input, output)

    def test_1356_0(self):
        input = search_input_pos([1, 3, 5, 6], 7)
        output = 0
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
