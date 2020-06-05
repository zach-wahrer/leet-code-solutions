import unittest


# Invalid solution
def compress_string_invalid(chars: list) -> int:
    if len(chars) < 2:
        return len(chars)

    array_length = 1
    char_count = 1
    p1, p2 = 0, 1

    while p2 < len(chars):
        print(p1, chars[p1], p2, chars[p2])
        if chars[p1] == chars[p2]:
            char_count += 1
        elif char_count == 1:
            p1 += 1
            array_length += 1

        else:
            if char_count < 10:
                p1 += 1
                chars[p1] = str(char_count)
                p1 += 1
            else:
                p1 += 1
                chars[p1] = str(char_count)[0]
                p1 += 1
                chars[p1] = str(char_count)[1]
                p1 += 1
            array_length += 2
            char_count = 1
        p2 += 1

    if char_count > 1:
        p1 += 1
        if char_count < 10:
            chars[p1] = str(char_count)
            p1 += 1
            array_length += 1
        else:
            chars[p1] = str(char_count)[0]
            p1 += 1
            chars[p1] = str(char_count)[1]
            p1 += 1
            array_length += 2

    return array_length


# O(n) time and space solution
def compress_string(chars: list) -> int:
    if len(chars) < 2:
        return len(chars)

    char_count = 1
    p1, p2 = 0, 1
    queue = []

    def add_to_queue(char: int, count: int, queue: list):
        queue.append(char)
        if count > 1:
            for i in str(count):
                queue.append(i)
        return queue

    while p2 < len(chars):
        if chars[p1] == chars[p2]:
            char_count += 1
        else:
            queue = add_to_queue(chars[p1], char_count, queue)
            char_count = 1
            p1 = p2
        p2 += 1

    queue = add_to_queue(chars[p1], char_count, queue)

    for position, value in enumerate(queue):
        chars[position] = value

    return len(queue)


class TestCompress(unittest.TestCase):

    def test_aaabbaa(self):
        string = ["a", "a", "a", "b", "b", "a", "a"]
        input = compress_string(string)
        self.assertEqual((input, string), (6, ["a", "3", "b", "2", "a", "2", "a"]))

    def test_a2b2c3(self):
        string = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
        input = compress_string(string)
        self.assertEqual((input, string), (6, ['a', '2', 'b', '2', 'c', '3', 'c']))

    def test_a(self):
        string = ['a']
        input = compress_string(string)
        self.assertEqual((input, string), (1, ['a']))

    def test_large(self):
        string = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        input = compress_string(string)
        self.assertEqual(
            (input, string), (4, ["a", "b", "1", "2", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))

    def test_abbc(self):
        string = ['a', 'b', 'b', 'c']
        input = compress_string(string)
        self.assertEqual((input, string), (4, ['a', 'b', '2', 'c']))

    def test_ab(self):
        string = ['a', 'b']
        input = compress_string(string)
        self.assertEqual((input, string), (2, ['a', 'b']))

    def test_abc(self):
        string = ['a', 'b', 'c']
        input = compress_string(string)
        self.assertEqual((input, string), (3, ['a', 'b', 'c']))


if __name__ == '__main__':
    unittest.main()
