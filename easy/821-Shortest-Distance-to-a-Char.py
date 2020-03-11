import unittest


# O(n**2) time, O(1) space solution
def shortest_distance(S: str, C: str) -> list:

    def _distance_to_target(pos, string, target, direction):
        count = 0
        while True:
            if string[pos] == target:
                return count

            if direction == 'L':
                pos -= 1
            else:
                pos += 1
            count += 1

            if pos > len(string) - 1 or pos < 0:
                return -1

    distance = []

    for pos, char in enumerate(S):
        if char != C:
            left = _distance_to_target(pos, S, C, 'L')
            right = _distance_to_target(pos, S, C, 'R')
            if left != -1 and right != -1:
                space = min(left, right)
            else:
                space = max(left, right)
        else:
            space = 0

        distance.append(space)

    return distance


# O(n) solution
def shortest_distance(S: str, C: str) -> list:
    answer_left, answer_right = [], []
    last_seen = float('-inf')

    for pos, char in enumerate(S):
        if char == C:
            answer_left.append(0)
            last_seen = pos

        else:
            answer_left.append(pos - last_seen)

    last_seen = float('inf')
    for pos, char in enumerate(S[::-1]):
        if char == C:
            answer_right.append(0)
            last_seen = pos
        else:
            answer_right.append(pos - last_seen)

    answer = []
    for left, right in zip(answer_left, answer_right[::-1]):
        if type(left) is not float and type(right) is not float:
            answer.append(min(left, right))
        elif type(right) is not float:
            answer.append(right)
        else:
            answer.append(left)

    return answer


class TestDistance(unittest.TestCase):

    def test_loveleetcode_e(self):
        input = shortest_distance("loveleetcode", 'e')
        self.assertEqual(input, [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])

    def test_ideclarebankruptcy_a(self):
        input = shortest_distance("ideclarebankruptcy", 'a')
        self.assertEqual(input, [5, 4, 3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_aabaaba_b(self):
        input = shortest_distance('aabaaba', 'b')
        self.assertEqual(input, [2, 1, 0, 1, 1, 0, 1])

    def test_a_a(self):
        input = shortest_distance('a', 'a')
        self.assertEqual(input, [0])

    def test_aaaaaa_a(self):
        input = shortest_distance('aaaaaa', 'a')
        self.assertEqual(input, [0, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
