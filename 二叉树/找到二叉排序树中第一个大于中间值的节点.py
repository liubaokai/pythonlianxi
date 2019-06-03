def get_Min(root):
    if root is None:
        return root
    if root.lchild is not None:
        root = root.lchild
    return root

def get_Max(root):
    if root is None:
        return root
    if root.rchild is not None:
        root = root.rchild
    return root

def get_node(root):
    max_node = get_Max(root)
    min_node = get_Min(root)
    mid_node = (max_node + min_node) // 2
    while root is not None:
        if root.data <= mid_node:
            root = root.rchild
        else:
            result = root
            root = root.lchild
    return result
