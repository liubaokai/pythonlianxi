def find_way(root, num, sums, v):
    sums += root.data
    v.append(root.data)
    if root.lchild is None and root.rchild is None and sums == num:
        i = 0
        while i < len(v):
            print(v[i])
            i += 1
    if root.lchild is not None:
        find_way(root.lchild, num, sums, v)
    if root.rchild is not None:
        find_way(root.rchild, num, sums, v)
    sum -= v[-1]  # 因为不满足路径条件，所以要删除
    v.remove(v[-1])


def findpath(root, num):
    if not root:
        return []
    if root and not root.left and not root.right and root.val == num:
        return [[root.val]]
    res = []
    left = findpath(root.left, num - root.val)
    right = findpath(root.right, num - root.val)
    for i in left + right:
        res.append([root.val] + i)
    return res
