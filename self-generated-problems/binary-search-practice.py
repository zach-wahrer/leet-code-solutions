import unittest


def binary_search(input: list, target: int):
    start = 0
    finish = len(input) - 1

    while start <= finish:
        middle = (start + finish) // 2
        if input[middle] == target:
            return True
        if input[middle] > target:
            finish = middle - 1
        else:
            start = middle + 1

    return False


class TestBinarySearch(unittest.TestCase):
    def test_1_1000_true(self):
        test_input = list(range(1001))
        self.assertTrue(binary_search(test_input, 700))

    def test_1_1000_false(self):
        test_input = list(range(1001))
        test_input.remove(300)
        self.assertFalse(binary_search(test_input, 300))


if __name__ == "__main__":
    unittest.main()
