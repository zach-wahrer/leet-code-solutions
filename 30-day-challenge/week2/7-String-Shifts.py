import unittest


# O(n) solution using slices
def shift_string(s: str, shift: list) -> str:
    def _get_final_shift(shifts: list):
        amount = 0
        for shift in shifts:
            if shift[0] == 1:
                amount += shift[1]
            else:
                amount -= shift[1]

        return (1, amount % len(s)) if amount > 0 else (0, abs(amount) % len(s))

    def _shift_string(shift_instruction, string):
        print(shift_instruction)
        if shift_instruction[0] == 1:
            return string[-shift_instruction[1]:] + string[:-shift_instruction[1]]
        else:
            return string[shift_instruction[1]:] + string[:shift_instruction[1]]

    return _shift_string(_get_final_shift(shift), s)


# O(n) solution using slices - Improved
def shift_string(s: str, shift: list) -> str:
    def _get_final_shift(shifts: list):
        amount = 0
        for shift in shifts:
            if shift[0] == 1:
                amount += shift[1]
            else:
                amount -= shift[1]

        return amount

    def _shift_string(amount, string):
        move = abs(amount) % len(string)
        if amount > 0:
            return string[-move:] + string[:-move]
        else:
            return string[move:] + string[:move]

    return _shift_string(_get_final_shift(shift), s)


class TestStringShift(unittest.TestCase):
    def test_xqgwkiqpif(self):
        self.assertEqual(shift_string("xqgwkiqpif",
                                      [[1, 4], [0, 7], [0, 8], [0, 7], [0, 6], [1, 3], [0, 1], [1, 7], [0, 5], [0, 6]]), "qpifxqgwki")

    def test_mecsk(self):
        self.assertEqual(shift_string("mecsk",
                                      [[1, 4], [0, 5], [0, 4], [1, 1], [1, 5]]), 'kmecs')

    def test_abc(self):
        self.assertEqual(shift_string('abc', [[0, 1], [1, 2]]), 'cab')

    def test_abc2(self):
        self.assertEqual(shift_string('abc', [[0, 1]]), 'bca')

    def test_abcdefg(self):
        self.assertEqual(shift_string('abcdefg',
                                      [[1, 1], [1, 1], [0, 2], [1, 3]]), 'efgabcd')

    def test_a(self):
        self.assertEqual(shift_string('a',
                                      [[0, 3]]), 'a')


if __name__ == "__main__":
    unittest.main()
