'''
Psudocode:
    Split into words
    Return length of last word
'''

import unittest


def len_last_word(s: str) -> int:
    words = s.split()
    if words:
        return len(words[-1])
    else:
        return 0


class TestLastWordLength(unittest.TestCase):

    def test_Hello_World(self):
        input = len_last_word("Hello World")
        output = 5
        self.assertEqual(input, output)

    def test_Evil_Empire(self):
        input = len_last_word("Evil Empire")
        output = 6
        self.assertEqual(input, output)

    def test_All_your_base_are_belong_to_us(self):
        input = len_last_word(" All your base are belong to us ")
        output = 2
        self.assertEqual(input, output)

    def test_Hiya(self):
        input = len_last_word("Hiya")
        output = 4
        self.assertEqual(input, output)

    def test_blank(self):
        input = len_last_word("")
        output = 0
        self.assertEqual(input, output)

    def test_space(self):
        input = len_last_word(" ")
        output = 0
        self.assertEqual(input, output)

    def test_multi_space(self):
        input = len_last_word("        ")
        output = 0
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
