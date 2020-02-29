import unittest
from models.binary_tree import TreeNode


def same_tree(p: TreeNode, q: TreeNode) -> bool:
    pass


class TestSameTree(unittest.TestCase):

    def test_sym_true(self):
        tree1 = TreeNode()
        tree2 = TreeNode()
        tree1.build_from_heap([1, 2, 3])
        tree2.build_from_heap([1, 2, 3])
        self.assertTrue(same_tree(tree1, tree2))

    def test_small_asym_false(self):
        tree1 = TreeNode()
        tree2 = TreeNode()
        tree1.build_from_heap([1, 2])
        tree2.build_from_heap([1, None, 2])
        self.assertFalse(same_tree(tree1, tree2))

    def test_sym_false(self):
        tree1 = TreeNode()
        tree2 = TreeNode()
        tree1.build_from_heap([1, 2, 1])
        tree2.build_from_heap([1, 1, 2])
        self.assertFalse(same_tree(tree1, tree2))

    def test_blank_false(self):
        tree1 = TreeNode()
        tree2 = TreeNode()
        tree1.build_from_heap([1, 2, 3, 4])
        tree2.build_from_heap([])
        self.assertFalse(same_tree(tree1, tree2))

    def test_blank2_true(self):
        tree1 = TreeNode()
        tree2 = TreeNode()
        tree1.build_from_heap([])
        tree2.build_from_heap([])
        self.assertTrue(same_tree(tree1, tree2))

    def test_one_true(self):
        tree1 = TreeNode()
        tree2 = TreeNode()
        tree1.build_from_heap([1])
        tree2.build_from_heap([1])
        self.assertTrue(same_tree(tree1, tree2))

    def test_two_false(self):
        tree1 = TreeNode()
        tree2 = TreeNode()
        tree1.build_from_heap([1])
        tree2.build_from_heap([2])
        self.assertTrue(same_tree(tree1, tree2))
