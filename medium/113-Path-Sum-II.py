import unittest
from models.binary_tree import TreeNode


# Recursive
def path_sum(root: TreeNode, sum: int) -> list:
    if not root:
        return []

    final_paths = []

    def _path_sum(node, acc_sum, curr_path, req_sum):
        if not node.left and not node.right:
            if node.val + acc_sum == req_sum:
                final_paths.append(curr_path + [node.val])
                return

        if node.left:
            _path_sum(node.left, acc_sum + node.val, curr_path + [node.val], req_sum)

        if node.right:
            _path_sum(node.right, acc_sum + node.val, curr_path + [node.val], req_sum)

    _path_sum(root, 0, [], sum)

    return final_paths


class TestPathSum(unittest.TestCase):

    def test_two_paths_22(self):
        tree = TreeNode()
        tree.build_from_heap([5, 4, 8, 11, None, 13, 4, 7, 2,
                              None, None, None, None, 5, 1])
        self.assertEqual(path_sum(tree, 22), [[5, 4, 11, 2], [5, 8, 4, 5]])

    def test_two_paths_none(self):
        tree = TreeNode()
        tree.build_from_heap([6, 4, 8, 11, None, 13, 4, 7, 2,
                              None, None, None, None, 5, 1])
        self.assertEqual(path_sum(tree, 22), [])

    def test_one_path_26(self):
        tree = TreeNode()
        tree.build_from_heap([5, 4, 8, 11, None, 13, 4, 7, 2,
                              None, None, None, None, 5, 1])
        self.assertEqual(path_sum(tree, 26), [[5, 8, 13]])

    def test_short_5(self):
        tree = TreeNode()
        tree.build_from_heap([5])
        self.assertEqual(path_sum(tree, 5), [[5]])

    def test_short_5(self):
        tree = TreeNode()
        tree.build_from_heap([2, 3, 3])
        self.assertEqual(path_sum(tree, 5), [[2, 3], [2, 3]])


if __name__ == "__main__":
    unittest.main()
