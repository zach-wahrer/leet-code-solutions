import unittest
from models.binary_tree import TreeNode


def same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True

    if not p and q or not q and p:
        return False

    def dfs_tree(node: TreeNode) -> TreeNode:
        yield node
        if node.left:
            yield from dfs_tree(node.left)
        if node.right:
            yield from dfs_tree(node.right)

    for tree1, tree2 in zip(dfs_tree(p), dfs_tree(q)):
        if tree1.val != tree2.val or bool(tree1.left) != bool(tree2.left) or \
                bool(tree1.right) != bool(tree2.right):
            return False

    return True


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
        self.assertFalse(same_tree(tree1, tree2))


if __name__ == "__main__":
    unittest.main()
