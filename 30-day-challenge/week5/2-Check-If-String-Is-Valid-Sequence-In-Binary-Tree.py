import unittest
from binaryTree import TreeNode


def sequence_in_tree(root: TreeNode, arr: list) -> bool:
    pass


class TestStringInTree(unittest.TestCase):
    def test_0101(self):
        root = TreeNode()
        root.build_from_heap([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0])
        self.assertTrue(sequence_in_tree(root, [0, 1, 0, 1]))

    def test_000(self):
        root = TreeNode()
        root.build_from_heap([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0])
        self.assertTrue(sequence_in_tree(root, [0, 0, 0]))

    def test_001(self):
        root = TreeNode()
        root.build_from_heap([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0])
        self.assertFalse(sequence_in_tree(root, [0, 0, 1]))

    def test_011(self):
        root = TreeNode()
        root.build_from_heap([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0])
        self.assertFalse(sequence_in_tree(root, [0, 1, 1]))


if __name__ == "__main__":
    unittest.main()
