import unittest


def replace_elements(arr: list) -> list:
    pass


class TestReplaceElements(unittest.TestCase):
    def test_short(self):
        arr = [17, 18, 5, 4, 6, 1]
        output = [18, 6, 6, 6, 1, -1]
        self.assertEqual(replace_elements(arr), output)
