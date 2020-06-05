import unittest


# O(n**2) time solution
def smash_stones_quadradic(stones: list) -> int:
    def _pop_heaviest(stones):
        heaviest = max(stones)
        stones.remove(heaviest)
        return heaviest

    while len(stones) >= 1:
        if len(stones) == 1:
            return stones[0]

        heaviest = _pop_heaviest(stones)
        sec_heaviest = _pop_heaviest(stones)

        if heaviest != sec_heaviest:
            stones.append(heaviest - sec_heaviest)

    return 0


# O(n log n) time heap queue solution
def smash_stones(stones: list) -> int:
    import heapq

    p_queue = [-stone for stone in stones]
    heapq.heapify(p_queue)

    while len(p_queue) >= 1:
        if len(p_queue) == 1:
            return abs(p_queue[0])

        heaviest = heapq.heappop(p_queue)
        sec_heaviest = heapq.heappop(p_queue)

        if heaviest != sec_heaviest:
            heapq.heappush(p_queue, heaviest - sec_heaviest)

    return 0


class TestStones(unittest.TestCase):
    def test_274181(self):
        self.assertEqual(smash_stones([2, 7, 4, 1, 8, 1]), 1)

    def test_22(self):
        self.assertEqual(smash_stones([2, 2]), 0)

    def test_222(self):
        self.assertEqual(smash_stones([2, 2, 2]), 2)

    def test_10(self):
        self.assertEqual(smash_stones([10]), 10)


if __name__ == "__main__":
    unittest.main()
