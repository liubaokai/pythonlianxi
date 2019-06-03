def creat_doubletree(root):
    if root is None:
        return None
    doutree = bitnode()
    doutree.data = root.data
    doutree.lchild = creat_doubletree(root.lchild)
    doutree.rchild = creat_doubletree(root.rchild)
    return doutree
