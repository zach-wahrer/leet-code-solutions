from models.binary_tree import TreeNode
import unittest


# Recursive DFS solution O(b**d)?? time
def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    def _max_depth(node, current_depth, max_depth):
        if node.left is None:
            max_depth.append(current_depth)
        else:
            _max_depth(node.left, current_depth + 1, max_depth)
        if node.right is None:
            max_depth.append(current_depth)
        else:
            _max_depth(node.right, current_depth + 1, max_depth)

    max_depth = [1]
    current_depth = 2

    if root.left:
        _max_depth(root.left, current_depth, max_depth)
    if root.right:
        _max_depth(root.right, current_depth, max_depth)

    return max(max_depth)


class TestMaxDepth(unittest.TestCase):

    def test_3920157_3(self):
        tree = TreeNode()
        tree.build_from_heap([3, 9, 20, None, None, 15, 7])
        self.assertEqual(max_depth(tree), 3)

    def test_3_1(self):
        tree = TreeNode()
        tree.build_from_heap([3])
        self.assertEqual(max_depth(tree), 1)

    def test_long_4(self):
        tree = TreeNode()
        tree.build_from_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(max_depth(tree), 4)

    def test_blank_0(self):
        tree = []
        self.assertEqual(max_depth(tree), 0)


if __name__ == "__main__":
    unittest.main()
