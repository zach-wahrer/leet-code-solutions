import unittest
from collections import deque


# Initial solution - O(n) because of _refresh_value's remove()
class LRUCache:

    def __init__(self, capacity: int):
        self.LRU_queue = deque(["" for i in range(capacity)])
        self.value_store = {}

    def get(self, key: int) -> int:
        if key in self.value_store:
            self._refresh_value(key)
            return self.value_store[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.value_store:
            self._refresh_value(key)
        else:
            oldest_value = self.LRU_queue.popleft()
            if oldest_value in self.value_store:
                self.value_store.pop(oldest_value)
            self.LRU_queue.append(key)

        self.value_store[key] = value

    def _refresh_value(self, key: int) -> None:
        self.LRU_queue.remove(key)
        self.LRU_queue.append(key)


class TestLRUCache(unittest.TestCase):
    def test_operations(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)


if __name__ == "__main__":
    unittest.main()
