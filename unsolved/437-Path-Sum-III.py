import unittest
from models.binary_tree import TreeNode, preorder


# Recursive
def path_sum(root: TreeNode, sum: int) -> int:
    if not root:
        return 0

    sum_attained = []

    def _path_sum(node, path_value):
        print(node.val)
        if path_value + node.val == sum:
            print("Adding ", node.val, path_value)
            sum_attained.append(1)
        if node.left:
            _path_sum(node.left, path_value + node.val)
            _path_sum(node.left, 0)

        if node.right:
            _path_sum(node.right, 0)
            _path_sum(node.right, path_value + node.val)

    _path_sum(root, 0)

    return sum_attained.count(1)


class TestPathSum(unittest.TestCase):

    def test_3_2(self):
        tree = TreeNode()
        tree.build_from_heap([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None,
                              4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5])
        self.assertEqual(path_sum(tree, 3), 2)

    # def test_8_3(self):
    #     tree = TreeNode()
    #     tree.build_from_heap([10, 5, -3, 3, 2, 0, 11, 3, -2, None, 1])
    #     self.assertEqual(path_sum(tree, 8), 3)
    #
    # def test_15_1(self):
    #     tree = TreeNode()
    #     tree.build_from_heap([10, 5, -3, 3, 2, 0, 11, 3, -2, None, 1])
    #     self.assertEqual(path_sum(tree, 15), 1)
    #
    # def test_9_2(self):
    #     tree = TreeNode()
    #     tree.build_from_heap([10, 5, -3, 4, 4, 0, 11, 3, -2, None, 1])
    #     self.assertEqual(path_sum(tree, 9), 2)
    #
    # def test_2_1(self):
    #     tree = TreeNode()
    #     tree.build_from_heap([1, 1])
    #     self.assertEqual(path_sum(tree, 2), 1)
    #
    # def test_10_0(self):
    #     tree = TreeNode()
    #     tree.build_from_heap([1, 2, 3, 4])
    #     self.assertEqual(path_sum(tree, 10), 0)
    #
    # def test_blank(self):
    #     tree = TreeNode()
    #     tree.build_from_heap([])
    #     self.assertEqual(path_sum(tree, 4), 0)
    #
    # def test_1_4(self):
    #     tree = TreeNode()
    #     tree.build_from_heap([0, 1, 1])
    #     self.assertEqual(path_sum(tree, 1), 4)


if __name__ == "__main__":
    unittest.main()
