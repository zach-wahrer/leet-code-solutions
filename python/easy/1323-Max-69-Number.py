import unittest


# O(n) time and space solution
def max_69_num(num: int) -> int:
    num_list = list(str(num))
    for index, digit in enumerate(num_list):
        if digit == "6":
            num_list[index] = "9"
            break

    return int("".join(num_list))


class TestMax69(unittest.TestCase):
    def test_9669(self):
        self.assertEqual(max_69_num(9669), 9969)

    def test_9996(self):
        self.assertEqual(max_69_num(9996), 9999)

    def test_9999(self):
        self.assertEqual(max_69_num(9999), 9999)

    def test_6(self):
        self.assertEqual(max_69_num(6), 9)

    def test_96(self):
        self.assertEqual(max_69_num(96), 99)


if __name__ == "__main__":
    unittest.main()
