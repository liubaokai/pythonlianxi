def construct_tree(preorder=None, inorder=None):
    if not preorder or not inorder:
        return None
    index = inorder.index(preorder[0])
    left = inorder[0:index]
    right = inorder[index + 1:]
    root = TreeNode(preorder[0])
    root.left = construct_tree(preorder[1:1 + len(left), left])
    root.right = construct_tree(preorder[-len(right):], right)
    return root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
