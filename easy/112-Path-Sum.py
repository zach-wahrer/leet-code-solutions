import unittest
from models.binarytree import TreeNode


# Recursive
def path_sum(root: TreeNode, sum: int) -> bool:
    pass


class TestPathSum(unittest.TestCase):

    def test_22_true(self):
        tree = TreeNode()
        tree.build_from_heap([5, 4, 8, 11, None, 13, 4, 7, 2,
                              None, None, None, None, None, 1])
        self.assertTrue(path_sum(tree, 22))

    def test_26_true(self):
        tree = TreeNode()
        tree.build_from_heap([5, 4, 8, 11, None, 13, 4, 7, 2,
                              None, None, None, None, None, 1])
        self.assertTrue(path_sum(tree, 26))

    def test_1000_false(self):
        tree = TreeNode()
        tree.build_from_heap([5, 4, 8, 11, None, 13, 4, 7, 2,
                              None, None, None, None, None, 1])
        self.assertFalse(path_sum(tree, 1000))

    def test_1_true(self):
        tree = [1]
        self.assertTrue(path_sum(tree, 1))

    def test_1_false(self):
        tree = [1]
        self.assertFalse(path_sum(tree, 20))

    def test_blank_false(self):
        tree = []
        self.assertFalse(path_sum(tree, 14))
