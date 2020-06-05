import unittest


# O(1) space and time solution
def num_1_bits(n: int) -> int:
    one_count = 0
    for i in list(bin(n))[2:]:
        if i == "1":
            one_count += 1

    return one_count


class TestNum1Bits(unittest.TestCase):
    def test_11(self):
        self.assertEqual(num_1_bits(11), 3)

    def test_128(self):
        self.assertEqual(num_1_bits(128), 1)

    def test_4294967293(self):
        self.assertEqual(num_1_bits(4294967293), 31)


if __name__ == "__main__":
    unittest.main()
