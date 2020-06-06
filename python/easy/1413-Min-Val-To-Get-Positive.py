import unittest

# O(n) time / O(1) space solution
def min_val_to_positive(nums: list) -> int:
    min_pos_value = 1
    running_total = 1

    for num in nums:
        current_value = num + running_total
        if current_value <= 0:
            min_pos_value += abs(current_value) + 1
            running_total += abs(current_value) + 1 + num
        else:
            running_total += num

    return min_pos_value


class TestMinValueToGetPositive(unittest.TestCase):
    def test_complex(self):
        nums = [-3, 2, -3, 4, 2]
        self.assertEqual(min_val_to_positive(nums), 5)

    def test_simple(self):
        nums = [1, 2]
        self.assertEqual(min_val_to_positive(nums), 1)

    def test_negatives(self):
        nums = [1, -2, -3]
        self.assertEqual(min_val_to_positive(nums), 5)


if __name__ == "__main__":
    unittest.main();
