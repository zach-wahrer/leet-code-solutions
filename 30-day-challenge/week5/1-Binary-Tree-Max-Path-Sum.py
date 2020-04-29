import unittest
from binaryTree import TreeNode


def max_path_sum(root: TreeNode) -> int:
    pass


class TestMaxPathSum(unittest.TestCase):
    def test_123(self):
        root = TreeNode()
        root.build_from_heap([1, 2, 3])
        self.assertEqual(max_path_sum(root), 6)

    def test_minus(self):
        root = TreeNode()
        root.build_from_heap([-10, 9, 20, None, None, 15, 7])
        self.assertEqual(max_path_sum(root), 42)


if __name__ == "__main__":
    unittest.main()
