import unittest


class MinStack:

    def __init__(self):
        self._min_val = float("inf")
        self._values = []

    def push(self, x: int) -> None:
        self._values.append(x)
        if x < self._min_val:
            self._min_val = x

    def pop(self) -> None:
        value = self._values.pop()
        if value == self._min_val and self._values:
            self._min_val = min(self._values)
        if not self._values:
            self._min_val = float("inf")
        return value

    def top(self) -> int:
        return self._values[-1]

    def getMin(self) -> int:
        return self._min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class TestMinStack(unittest.TestCase):
    def test_min(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3)
        stack.pop()
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.getMin(), -2)

    def test_min_2(self):
        stack = MinStack()
        stack.push(-2)
        self.assertEqual(stack.getMin(), -2)
        self.assertEqual(stack.pop(), -2)
        self.assertEqual(stack._min_val, float("inf"))
        self.assertEqual(stack._values, [])


if __name__ == "__main__":
    unittest.main()
