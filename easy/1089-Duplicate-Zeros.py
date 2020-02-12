import unittest


# One pass solution, O(n(logn)) time, O(n(logn)) space
# Loop through arr.
# If number is 0, create a slice of remaining list and copy it over remaining
# Put a 0 in the next space
def duplicate_zeros_logn(arr: list) -> None:
    i = 0
    array_length = len(arr)
    while i < array_length:
        if arr[i] == 0 and i + 1 < array_length:
            slice = arr[i + 1:-1]
            i += 1
            if i < array_length:
                arr[i] = 0
                arr[i + 1:] = slice
        i += 1
    return arr


# One pass solution, O(n) time and space
def duplicate_zeros(arr: list) -> None:
    from collections import deque
    i, queue = 0, deque()
    array_length = len(arr)
    while i < array_length:
        if queue:
            queue.append(arr[i])
            arr[i] = queue.popleft()
        if arr[i] == 0 and i + 1 < array_length:
            queue.append(arr[i + 1])
            i += 1
            arr[i] = 0
        i += 1
    return arr


class TestDuplicateZeros(unittest.TestCase):

    def test_10230450(self):
        input = duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])
        self.assertEqual(input, [1, 0, 0, 2, 3, 0, 0, 4])

    def test_123(self):
        input = duplicate_zeros([1, 2, 3])
        self.assertEqual(input, [1, 2, 3])

    def test_8(self):
        input = duplicate_zeros([8])
        self.assertEqual(input, [8])

    def test_10(self):
        input = duplicate_zeros([1, 0])
        self.assertEqual(input, [1, 0])

    def test_8(self):
        input = duplicate_zeros([0])
        self.assertEqual(input, [0])

    def test_0909(self):
        input = duplicate_zeros([0, 9, 0, 9])
        self.assertEqual(input, [0, 0, 9, 0])

    def test_blank(self):
        input = duplicate_zeros([])
        self.assertEqual(input, [])


if __name__ == "__main__":
    unittest.main()
