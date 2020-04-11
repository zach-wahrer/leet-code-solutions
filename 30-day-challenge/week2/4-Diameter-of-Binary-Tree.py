import unittest
from binaryTree import TreeNode


def diameter_binary_tree(root: TreeNode) -> int:
    pass


class TestBinaryTreeDiameter(unittest.TestCase):
    def test_tree3(self):
        root = TreeNode()
        root.build_from_heap([1, 2, 3, 4, 5])
        self.assertEqual(diameter_binary_tree(root), 3)

    def test_tree1(self):
        root = TreeNode()
        root.build_from_heap([1, 2])
        self.assertEqual(diameter_binary_tree(root), 1)
