import unittest


# O(n) solution
def max_contig_array(nums: list) -> int:
    count = 0
    max_length = 0
    seen = {0: 0}
    for index, number in enumerate(nums, 1):
        if number == 0:
            count -= 1
        else:
            count += 1

        if count in seen:
            max_length = max(max_length, index - seen[count])
        else:
            seen[count] = index

    return max_length


class TestMaxContiguousArray(unittest.TestCase):
    def test_00100011(self):
        self.assertEqual(max_contig_array([0, 0, 1, 0, 0, 0, 1, 1]), 6)

    # def test_01101110(self):
    #     self.assertEqual(max_contig_array([0, 1, 1, 0, 1, 1, 1, 0]), 4)
    #
    # def test_0001110(self):
    #     self.assertEqual(max_contig_array([0, 0, 0, 1, 1, 1, 0]), 6)
    #
    # def test_01(self):
    #     self.assertEqual(max_contig_array([0, 1]), 2)
    #
    # def test_010(self):
    #     self.assertEqual(max_contig_array([0, 1, 0]), 2)
    #
    # def test_0(self):
    #     self.assertEqual(max_contig_array([0]), 0)
    #
    # def test_00(self):
    #     self.assertEqual(max_contig_array([0, 0]), 0)
    #
    # def test_0110(self):
    #     self.assertEqual(max_contig_array([0, 1, 1, 0]), 4)
    #
    # def test_1110(self):
    #     self.assertEqual(max_contig_array([1, 1, 1, 0]), 2)


if __name__ == "__main__":
    unittest.main()
