def find_max_sub_tree(root, max_root):
    '''都需要要用到递归才行'''
    if root is None:
        return None
    lmax = find_max_sub_tree(root.lchild, max_root)
    rmax = find_max_sub_tree(root.rchild, max_root)
    sums = lmax + rmax + root.data
    if sums > maxsum:
        maxsum = sums
        max_root.data = root.data
    return sums
