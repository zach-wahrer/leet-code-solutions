import unittest


# O(n) time/space solution
def fizz_buzz(n: int) -> list:
    output = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output.append('FizzBuzz')
        elif i % 3 == 0:
            output.append('Fizz')
        elif i % 5 == 0:
            output.append('Buzz')
        else:
            output.append(str(i))

    return output


# Reorganized O(n) time/space solution
def fizz_buzz(n: int) -> list:
    output = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                output.append('FizzBuzz')
            else:
                output.append('Fizz')
        elif i % 5 == 0:
            output.append('Buzz')
        else:
            output.append(str(i))

    return output


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


if __name__ == "__main__":
    unittest.main()
