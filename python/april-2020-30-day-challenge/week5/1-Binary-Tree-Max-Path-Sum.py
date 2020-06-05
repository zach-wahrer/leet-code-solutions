import unittest
from binaryTree import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum

    def dfs(self, node):
        if not node:
            return 0

        left_subtree_sum = max(0, self.dfs(node.left))
        right_subtree_sum = max(0, self.dfs(node.right))
        self.max_sum = max(self.max_sum, left_subtree_sum + right_subtree_sum + node.val)

        return max(left_subtree_sum, right_subtree_sum) + node.val


class TestMaxPathSum(unittest.TestCase):
    def test_123(self):
        root = TreeNode()
        root.build_from_heap([1, 2, 3])
        solution = Solution()
        self.assertEqual(solution.maxPathSum(root), 6)

    def test_minus(self):
        root = TreeNode()
        root.build_from_heap([-10, 9, 20, None, None, 15, 7])
        solution = Solution()
        self.assertEqual(solution.maxPathSum(root), 42)


if __name__ == "__main__":
    unittest.main()
