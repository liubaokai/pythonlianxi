def get_path(root, node, stack):
    if root is None:
        return False
    if root == node:
        stack.push(root)
        return True
    if get_path(root.lchild, node, stack) or get_path(root.rchild, node, stack):
        stack.push(node)
        return True
    return False

def find_parents(root, node1, node2):
    stack1 = stack()
    stack2 = stack()
    get_path(root, node1, stack1)
    get_path(root, node2, stack2)
    parents = stack1.peek()
    while stack1.peek() == stack2.peek():
        parents = stack1.peek()
        stack1.pop()
        stack2.pop()
    return parents

# '''-------------------------------------------------------------------------------------------'''

'''转换为后序遍历处理,不明白
'''
def get_baba(root, node1, node2):
    if root is None or node1 == root or node2 == root:
        return root
    lchild = get_path(root.lchild, node1, node2)
    rchild = get_path(root.rchild, node1, node2)
    if lchild is None:
        return rchild
    elif rchild is None:
        return lchild
    else:
        return root