def sub_tree(tree1, tree2):
    if tree1 and tree2:
        if tree1.val == tree2.val:
            return sub_tree(tree1.val, tree2.val) and sub_tree(tree1.val, tree2.val)
        else:
            return sub_tree(tree1.left, tree2) or sub_tree(tree1.right, tree2)
    if not tree1 and tree2:
        return False
    return True


