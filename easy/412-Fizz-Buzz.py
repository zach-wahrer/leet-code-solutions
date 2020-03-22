import unittest


def fizz_buzz(n: int) -> list:
    pass


class TestFizzBuzz(unittest.TestCase):

    def test_15(self):
        output = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ]
        self.assertEqual(fizz_buzz(15), output)


def test_blank(self):
    self.assertEqual(fizz_buzz(0), [])


def test_1(self):
    self.assertEqual(fizz_buzz(1), ['1'])
