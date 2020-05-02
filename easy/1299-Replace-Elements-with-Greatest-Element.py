import unittest


# O(n**2) time solution
def replace_elements(arr: list) -> list:
    for index in range(len(arr)):
        if index == len(arr) - 1:
            arr[index] = -1
        else:
            arr[index] = max(arr[index + 1:])

    return arr


class TestReplaceElements(unittest.TestCase):
    def test_short(self):
        arr = [17, 18, 5, 4, 6, 1]
        output = [18, 6, 6, 6, 1, -1]
        self.assertEqual(replace_elements(arr), output)

    def test_easy(self):
        arr = [1, 2, 3, 4]
        output = [4, 4, 4, -1]
        self.assertEqual(replace_elements(arr), output)

    def test_one(self):
        arr = [1]
        output = [-1]
        self.assertEqual(replace_elements(arr), output)


if __name__ == "__main__":
    unittest.main()
