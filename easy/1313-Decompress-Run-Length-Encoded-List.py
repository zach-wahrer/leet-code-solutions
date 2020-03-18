import unittest


# O(n) solution
def decompress_list(nums: list) -> list:
    output = []
    p1, p2 = 0, 1

    while p2 < len(nums):
        for _ in range(nums[p1]):
            output.append(nums[p2])
        p1 += 2
        p2 += 2

    return output


class TestDecompress(unittest.TestCase):

    def test_1234(self):
        input = decompress_list([1, 2, 3, 4])
        self.assertEqual(input, [2, 4, 4, 4])

    def test_1123(self):
        input = decompress_list([1, 1, 2, 3])
        self.assertEqual(input, [1, 3, 3])

    def test_11(self):
        input = decompress_list([1, 1])
        self.assertEqual(input, [1])


if __name__ == '__main__':
    unittest.main()
