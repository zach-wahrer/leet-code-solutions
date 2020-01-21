'''
Psudocode:

'''

import unittest


def len_last_word(s: str) -> int:
    pass


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
        input = len_last_word("All your base are belong to us")
        output = 2
        self.assertEqual(input, output)

    def test_Hiya(self):
        input = len_last_word("Hiya")
        output = 4
        self.assertEqual(input, output)
