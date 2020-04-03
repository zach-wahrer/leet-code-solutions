from models.binaryTree import TreeNode


def traverse_in_order(node):
    if node.left:
        traverse_in_order(node.left)
    print(node.val)
    if node.right:
        traverse_in_order(node.right)


def find_kth_element(node: TreeNode, kth_smallest: int, status: dict):
    if node.left:
        status = find_kth_element(node.left, kth_smallest, status)
        if status['found']:
            return status

    status['count'] += 1
    if status['count'] == kth_smallest:
        return {'count': status['count'], 'found': node.val}

    if node.right:
        status = find_kth_element(node.right, kth_smallest, status)
        if status['found']:
            return status

    return {'count': status['count'], 'found': False}


root = TreeNode()
root.build_from_heap([10, 5, 14, 1, 6, 12, 15])
print(find_kth_element(root, 6, {'count': 0, 'found': False})['found'])
