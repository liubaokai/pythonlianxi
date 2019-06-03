def depth(root):
    if not root:
        return
    else:
        left = depth(root.left) + 1
        right = depth(root.right) + 1
        return max(left, right)
