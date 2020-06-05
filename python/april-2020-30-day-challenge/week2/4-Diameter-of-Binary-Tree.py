import unittest
from binaryTree import TreeNode


# Recursive solution
def diameter_binary_tree(root: TreeNode) -> int:

    def _tree_diameter(node):
        if not node:
            return [0, 0]

        left_diameter, longest_left = _tree_diameter(node.left)
        right_diameter, longest_right = _tree_diameter(node.right)
        current_diameter = longest_left + longest_right + 1

        return [max(left_diameter, right_diameter, current_diameter),
                max(longest_left, longest_right) + 1]

    return max(_tree_diameter(root)) - 1 if root else 0


class TestBinaryTreeDiameter(unittest.TestCase):
    def test_tree1432(self):
        root = TreeNode()
        root.build_from_heap([1, 4, 3, 2])
        self.assertEqual(diameter_binary_tree(root), 3)

    def test_tree3(self):
        root = TreeNode()
        root.build_from_heap([1, 2, 3, 4, 5])
        self.assertEqual(diameter_binary_tree(root), 3)

    def test_tree_long_left(self):
        root = TreeNode()
        root.build_from_heap([2, 3, None, 1])
        self.assertEqual(diameter_binary_tree(root), 2)

    def test_tree1(self):
        root = TreeNode()
        root.build_from_heap([1, 2])
        self.assertEqual(diameter_binary_tree(root), 1)

    def test_tree2(self):
        root = TreeNode()
        root.build_from_heap([1, 2, 3])
        self.assertEqual(diameter_binary_tree(root), 2)

    def test_tree_empty(self):
        root = TreeNode()
        root.build_from_heap([])
        self.assertEqual(diameter_binary_tree(root), 0)

    def test_tree_root_only(self):
        root = TreeNode()
        root.build_from_heap([1])
        self.assertEqual(diameter_binary_tree(root), 0)


if __name__ == "__main__":
    unittest.main()
