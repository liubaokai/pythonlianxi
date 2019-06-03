def isSym(pRoot):
    if not pRoot or (not pRoot.left and not pRoot.right):
        return True
    if not pRoot.left or not pRoot.right or pRoot.left.val != pRoot.right.val:
        return False

    def sym(left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return sym(left.left, right.right) and sym(left.right, right.left)
        return False

    return sym(pRoot.left, pRoot.right)
