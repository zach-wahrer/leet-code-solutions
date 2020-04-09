import unittest


def compare_strings(S: str, T: str) -> bool:

    def process_string(string) -> list:
        stack = []
        for i in string[::]:
            if i == "#" and stack:
                stack.pop()
            elif i != "#":
                stack.append(i)
        return stack

    return process_string(S) == process_string(T)


class TestStringCompare(unittest.TestCase):
    def test_ac_true(self):
        S = "ab#c"
        T = "ad#c"
        self.assertTrue(compare_strings(S, T))

    def test_blank_true(self):
        S = "ab##"
        T = "c#d#"
        self.assertTrue(compare_strings(S, T))

    def test_c_true(self):
        S = "a##c"
        T = "#a#c"
        self.assertTrue(compare_strings(S, T))

    def test_cb_false(self):
        S = "a#c"
        T = "b"
        self.assertFalse(compare_strings(S, T))

    def test_y_true(self):
        S = "y#fo##f"
        T = "y#f#o##f"
        self.assertTrue(compare_strings(S, T))


if __name__ == "__main__":
    unittest.main()
