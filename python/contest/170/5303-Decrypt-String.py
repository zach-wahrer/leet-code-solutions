import unittest


def freqAlphabets(s: str) -> str:
    import string
    alpha_map = dict(zip(range(1, 27), string.ascii_lowercase))
    len_s, out_string, i = len(s), "", 0
    while i < len_s:
        if i+2 < len_s and s[i+2] == "#":
            out_string += alpha_map[int(s[i] + s[i+1])]
            i += 3
        else:
            out_string += alpha_map[int(s[i])]
            i += 1
    return out_string


def freqAlphabetsGross(s: str) -> str:
    import string
    alpha_map = dict(zip(range(1, 27), string.ascii_lowercase))
    tmp_number, out_string = "", ""
    for pos, char in enumerate(s):
        if char == "#" or char == 0:
            out_string += alpha_map[int(str(s[pos-2] + s[pos-1]))]
        elif char == "1" or char == "2":
            if len(s) > pos+2:
                if s[pos+2] != "#" and s[pos+1] != "#":
                    out_string += alpha_map[int(char)]
            if len(s) == pos+2:
                if s[pos+1] != "#":
                    out_string += alpha_map[int(char)]
            if len(s) == pos+1:
                out_string += alpha_map[int(char)]

        elif int(char) >= 3 and int(char) <= 9:
            if len(s) > pos+2:
                if s[pos+2] != "#" and s[pos+1] != "#":
                    out_string += alpha_map[int(char)]
            if len(s) == pos+2:
                if s[pos+1] != "#":
                    out_string += alpha_map[int(char)]
            if len(s) == pos+1:
                out_string += alpha_map[int(char)]

    return out_string


class TestMap(unittest.TestCase):

    def test_10_11_12(self):
        input = freqAlphabets("10#11#12")
        output = "jkab"
        self.assertEqual(input, output)

    def test_1326(self):
        input = freqAlphabets("1326#")
        output = "acz"
        self.assertEqual(input, output)

    def test_25(self):
        input = freqAlphabets("25#")
        output = "y"
        self.assertEqual(input, output)

    def test_failure(self):
        input = freqAlphabets("26#11#418#5")
        output = "zkdre"
        self.assertEqual(input, output)

    def test_alphabet(self):
        input = freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")
        output = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(input, output)


unittest.main()
