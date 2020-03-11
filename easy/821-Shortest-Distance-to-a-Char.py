import unittest


def shortest_distance(S: str, C: str) -> list:
    pass


class TestDistance(unittest.TestCase):

    def test_loveleetcode_e(self):
        input = shortest_distance("loveleetcode", 'e')
        self.assertEqual(input, [3, 2, 1, 0, 0, 1, 2, 2, 1, 0])

    def test_ideclarebankruptcy_a(self):
        input = shortest_distance("ideclarebankruptcy", 'a')
        self.assertEqual(input, [5, 4, 3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_aabaaba_b(self):
        input = shortest_distance('aabaaba', 'b')
        self.assertEqual(input, [2, 1, 0, 1, 1, 0, 1])

    def test_a_a(self):
        input = shortest_distance('a', 'a')
        self.assertEqual(input, [0])


if __name__ == "__main__":
    unittest.main()
