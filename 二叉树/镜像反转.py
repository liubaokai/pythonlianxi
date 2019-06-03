
def reverse_tree(root):
    if root is None:
        return
    reverse_tree(root.lchild)
    reverse_tree(root.rchild)
    # tem = root.lchild
    # root.lchild = root.rchild
    # root.rchild = tem
    root.rchild, root.lchild = root.lchild, root.rchild
