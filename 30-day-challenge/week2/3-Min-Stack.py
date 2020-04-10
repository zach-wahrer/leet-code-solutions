import unittest


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


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


if __name__ == "__main__":
    unittest.main()
