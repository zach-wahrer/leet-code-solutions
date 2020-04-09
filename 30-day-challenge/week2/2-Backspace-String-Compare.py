import unittest


def compare_strings(S: str, T: str) -> bool:
    pass


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
        self.assertTrue(compare_strings(S, T))


if __name__ == "__main__":
    unittest.main()
