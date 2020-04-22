import unittest


# O(n) time/space solution
def num_subarrays_equal_k(nums: list, k: int) -> int:
    count, sum = 0, 0
    hash = {0: 1}
    for num in nums:
        sum += num
        if sum - k in hash:
            print('ping', sum - k)
            count += hash[sum - k]
        hash[sum] = hash.setdefault(sum, 0) + 1

    print(hash)
    return count


class TestSubarrays(unittest.TestCase):
    def test_111_2(self):
        self.assertEqual(num_subarrays_equal_k([1, 1, 1], 2), 2)


if __name__ == "__main__":
    unittest.main()
