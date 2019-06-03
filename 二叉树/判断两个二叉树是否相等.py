def is_equal(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is None:
        return False
    if root1 is None and root2 is not None:
        return False
    if root1.data == root2.data:
        return is_equal(root1.lchild, root2.lchild) and is_equal(root1.rchild, root2.rchild)
    else:
        return False
