import unittest
from binaryTree import TreeNode, print_preorder


# O(n) time, O(1) space recursive in-order solution
def sequence_in_tree(root: TreeNode, arr: list) -> bool:
    def _traverse_tree(node, level):
        if level > len(arr) - 1 or node.val != int(arr[level]):
            return False

        if not node.left and not node.right:
            if node.val == arr[level] and len(arr) - 1 == level:
                return True
            return False

        left, right = False, False
        if node.left:
            left = _traverse_tree(node.left, level + 1)
        if node.right:
            right = _traverse_tree(node.right, level + 1)

        return True if left or right else False

    return _traverse_tree(root, 0)


class TestStringInTree(unittest.TestCase):

    def test_29180(self):
        root = TreeNode()
        root = root.build([2, 9, 3, None, 1, None, 2, None, None, None, 8], root, 0)
        self.assertFalse(sequence_in_tree(root, [2, 9, 1, 8, 0]))

    def test_0035(self):
        root = TreeNode()
        root = root.build([0, 0, 1, 3, 4, 2, None, 5], root, 0)
        self.assertTrue(sequence_in_tree(root, [0, 0, 3, 5]))

    def test_0101(self):
        root = TreeNode()
        root = root.build([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0], root, 0)
        self.assertTrue(sequence_in_tree(root, [0, 1, 0, 1]))

    def test_001(self):
        root = TreeNode()
        root = root.build([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0], root, 0)
        self.assertFalse(sequence_in_tree(root, [0, 0, 1]))

    def test_011(self):
        root = TreeNode()
        root = root.build([0, 1, 0, 0, 1, 0, 8, 8, 1, 0, 0], root, 0)
        self.assertFalse(sequence_in_tree(root, [0, 1, 1]))


if __name__ == "__main__":
    unittest.main()
