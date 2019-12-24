import unittest


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        pass

    def multiply(self, x, y):
        pass

    def sum(self, numbers):  # Take in an array of nums
        pass

    def max(self, numbers):  # Find max of list of nums
        pass


my_calculator = Calculator()

print(my_calculator.add(2, 7))


class TestCalculator(unittest.TestCase):

    def test_add_zeroes(self):
        x = 0
        y = 0
        ans = 0
        self.assertEqual(Calculator().add(x, y), ans)

    def test_add_simple(self):
        x = 1
        y = 1
        ans = 2
        self.assertEqual(Calculator().add(x, y), ans)

    def test_add_five_five(self):
        x = 5
        y = 5
        ans = 10
        self.assertEqual(Calculator().add(x, y), ans)


if __name__ == "__main__":
    unittest.main()
