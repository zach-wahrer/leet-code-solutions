import unittest
from models.binary_tree import TreeNode, preorder


def invert_bin_tree(root: TreeNode) -> TreeNode:
    def _dfs_invert(node: TreeNode):

        if node.left and node.right:
            node.left, node.right = node.right, node.left
        elif node.left and not node.right:
            node.right, node.left = node.left, None
        elif node.right and not node.left:
            node.left, node.right = node.right, None

        if node.left:
            _dfs_invert(node.left)
        if node.right:
            _dfs_invert(node.right)

    if root:
        _dfs_invert(root)

    return root


class TestInvertTree(unittest.TestCase):

    def test_4271369(self):
        input_tree = TreeNode()
        input_tree.build_from_heap([4, 2, 7, 1, 3, 6, 9])
        test_tree = TreeNode()
        test_tree.build_from_heap([4, 7, 2, 9, 6, 3, 1])
        self.assertEqual(invert_bin_tree(input_tree), test_tree)

    def test_blank(self):
        input_tree = TreeNode()
        input_tree.build_from_heap([])
        test_tree = TreeNode()
        test_tree.build_from_heap([])
        self.assertEqual(invert_bin_tree(input_tree), test_tree)

    def test_single(self):
        input_tree = TreeNode()
        input_tree.build_from_heap([1])
        test_tree = TreeNode()
        test_tree.build_from_heap([1])
        self.assertEqual(invert_bin_tree(input_tree), test_tree)

    def test_small(self):
        input_tree = TreeNode()
        input_tree.build_from_heap([1, 2, 3])
        test_tree = TreeNode()
        test_tree.build_from_heap([1, 3, 2])
        self.assertEqual(invert_bin_tree(input_tree), test_tree)

    def test_small_2(self):
        input_tree = TreeNode()
        input_tree.build_from_heap([1, 2])
        test_tree = TreeNode()
        test_tree.build_from_heap([1, None, 2])
        self.assertEqual(invert_bin_tree(input_tree), test_tree)


if __name__ == "__main__":
    unittest.main()
