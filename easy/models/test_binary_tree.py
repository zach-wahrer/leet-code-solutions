from binary_tree import TreeNode, preorder

tree = TreeNode()
tree.build_from_heap(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
print('Tree1:')
preorder(tree)

tree2 = TreeNode()
tree2.build_from_heap([3, 9, 20, None, 1, 15, 7])
print('\nTree2:')
preorder(tree2)
