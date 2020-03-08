import unittest
from models.binary_tree import TreeNode


def path_sum(root: TreeNode, sum: int) -> int:
    pass


class TestPathSum(unittest.TestCase):

    def test_8_3(self):
        tree = TreeNode()
        tree.build_from_heap([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        self.assertEqual(path_sum(tree, 8), 3)

    def test_15_1(self):
        tree = TreeNode()
        tree.build_from_heap([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        self.assertEqual(path_sum(tree, 15), 1)

    def test_9_2(self):
        tree = TreeNode()
        tree.build_from_heap([10, 5, -3, 4, 4, None, 11, 3, -2, None, 1])
        self.assertEqual(path_sum(tree, 9), 2)

    def test_1_1(self):
        tree = TreeNode()
        tree.build_from_heap([1])
        self.assertEqual(path_sum(tree, 1), 1)

    def test_10_0(self):
        tree = TreeNode()
        tree.build_from_heap([1, 2, 3, 4])
        self.assertEqual(path_sum(tree, 10), 0)

    def test_blank(self):
        tree = TreeNode()
        tree.build_from_heap([])
        self.assertEqual(path_sum(tree, 4), 0)
