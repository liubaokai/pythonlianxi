def serialize(root):
    tree = [root]
    ch = []
    while len(tree) > 0:
        tem = tree.pop(0)
        if tem is None:
            ch.append('#')
        else:
            ch.append(str(tem.val) + '*')
            tree.append(tem.left)
            tree.append(tem.right)
    return ''.join(ch)


def Deserialize(self, s):
    list = s.split(',')
    return self.deserializeTree(list)


def deserializeTree(self, list):
    if len(list) <= 0:
        return None
    val = list.pop(0)
    root = None
    if val != '#':
        root = TreeNode(int(val))
        root.left = self.deserializeTree(list)
        root.right = self.deserializeTree(list)
    return root
