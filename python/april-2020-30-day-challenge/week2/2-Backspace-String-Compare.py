import unittest


# O(n + m) time / space solution
def compare_strings_stack(S: str, T: str) -> bool:

    def process_string(string) -> list:
        stack = []
        for i in string[::]:
            if i == "#" and stack:
                stack.pop()
            elif i != "#":
                stack.append(i)
        return stack

    return process_string(S) == process_string(T)


# Two pointer O(1) space solution, doesn't work for all test cases
def compare_strings(S: str, T: str) -> bool:
    p1, p2 = len(S) - 1, len(T) - 1
    S_skip, T_skip = 0, 0

    while p1 >= 0 and p2 >= 0:

        while p1 >= 0:
            if S[p1] == "#":
                S_skip += 1
                p1 -= 1
            else:
                if S_skip:
                    S_skip -= 1
                    p1 -= 1
                else:
                    break

        while p2 >= 0:
            if T[p2] == "#":
                T_skip += 1
                p2 -= 1
            else:
                if T_skip:
                    T_skip -= 1
                    p2 -= 1
                else:
                    break

        if S[p1] != T[p2]:
            return False

        p1 -= 1
        p2 -= 1

    return True


class TestStringCompare(unittest.TestCase):
    def test_ac_leet3(self):
        S = "nzp#o#g"
        T = "b#nzp#o#g"
        self.assertTrue(compare_strings(S, T))

    def test_ac_leet2(self):
        S = "bbbextm"
        T = "bbb#extm"
        self.assertFalse(compare_strings(S, T))

    def test_ac_leet(self):
        S = "isfcow#"
        T = "isfcog#w#"
        self.assertTrue(compare_strings(S, T))

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
