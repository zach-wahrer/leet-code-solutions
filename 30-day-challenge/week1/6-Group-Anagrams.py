import unittest


# Partial solution, fails some leet code tests
def group_anagrams(strs: list) -> list:
    from collections import deque, Counter
    inputs = strs
    word_counts = deque()
    for word in inputs:
        word_counts.append(Counter(word[::]))

    anagrams = []
    pointer = 1

    while len(word_counts) > 1:
        group = []
        group.append(inputs[0])

        while pointer < len(word_counts):

            is_anagram = True

            for letter in word_counts[0]:
                if not (letter in word_counts[pointer]
                        and word_counts[0][letter] == word_counts[pointer][letter]):
                    pointer += 1
                    is_anagram = False
                    break

            if is_anagram:
                group.append(inputs[pointer])
                del word_counts[pointer]
                del inputs[pointer]

            pointer += 1

        anagrams.append(group)
        pointer = 1

        if word_counts:
            word_counts.popleft()
        if inputs:
            del inputs[0]

    if inputs:
        anagrams.append([inputs[0]])

    print(anagrams)
    return anagrams


def group_anagrams(strs):
    dictionary = {}
    for word in strs:
        key = tuple(sorted(word))
        dictionary[key] = dictionary.get(key, []) + [word]

    return list(dictionary.values())


class TestGroup(unittest.TestCase):
    def test_blank(self):
        input = group_anagrams(['b', ''])
        output = [
            ["b"],
            [""]
        ]
        self.assertEqual(input, output)

    def test_six(self):
        input = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        output = [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]
        self.assertEqual(input, output)

    def test_seven(self):
        input = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat', 'tab'])
        output = [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat", "tab"]
        ]
        self.assertEqual(input, output)

    def test_bob(self):
        input = group_anagrams(['boo', 'bob'])
        output = [
            ['boo'],
            ['bob']
        ]
        self.assertEqual(input, output)

    def test_pup(self):
        input = group_anagrams(['pup', 'pup'])
        output = [
            ['pup', 'pup']
        ]
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
