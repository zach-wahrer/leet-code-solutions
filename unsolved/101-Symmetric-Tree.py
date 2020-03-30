import unittest
from models.binaryTree import TreeNode


def is_symmetric(root: TreeNode) -> bool:
    if not root:
        return True
    tree_rows = {}

    def _traverse_tree(node: TreeNode, tree_rows: list, level: int):
        if level not in tree_rows:
            tree_rows[level] = []

        if node.val is not None:
            tree_rows[level].append(node.val)

        if node.left is not None:
            _traverse_tree(node.left, tree_rows, level + 1)
            if node.right is None:
                if level + 1 not in tree_rows:
                    tree_rows[level + 1] = []
                tree_rows[level + 1].append(None)

        if node.right is not None:
            if node.left is None:
                if level + 1 not in tree_rows:
                    tree_rows[level + 1] = []
                tree_rows[level + 1].append(None)
            _traverse_tree(node.right, tree_rows, level + 1)

    _traverse_tree(root, tree_rows, 1)

    for index, values in enumerate(tree_rows.values()):
        if index > 0:
            if len(values) % 2 != 0 or len(values) != len(tree_rows[index]) * 2:
                return False
            first_half = values[:len(values) // 2]
            second_half = values[len(values) // 2:]
            second_half = second_half[::-1]

            if first_half != second_half:
                return False

    return True


class TestSymmetry(unittest.TestCase):

    def test_true(self):
        root = TreeNode()
        root.build_from_heap([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(is_symmetric(root))

    def test_false(self):
        root = TreeNode()
        root.build_from_heap([1, 2, 2, None, 3, None, 3])
        self.assertFalse(is_symmetric(root))

    def test_blank(self):
        root = TreeNode()
        self.assertTrue(is_symmetric(root))

    def test_leet(self):
        root = TreeNode()
        root.build_from_heap([2, 3, 3, 4, 5, 5, 4, None, None, 8, 9, None, None, 9, 8])
        self.assertFalse(is_symmetric(root))


if __name__ == "__main__":
    unittest.main()
