class Node():
    def  __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
def add_tree(val):
    node = Node(val)
    queue = [root]
    while queue:
        cur_node = queue.pop(0)
        if cur_node.left == None:
            cur_node.left = node
            return
        else:
            queue.append(cur_node.left)
        if cur_node.right == None:
            cur_node.right = node
            return
        else:
            queue.append(cur_node.right)


def pre_order(root):
    '''中左右'''
    if root == None:
        return
    queue = []
    node = root
    while queue or node:
        while node:
            print(node.val)
            queue.append(node)
            node = node.left
        node = queue.pop()
        node = node.right


def after_order(root):
   """后序就是 左右中  反过来就是中右左 先实现中右左，那么反向输出就可以了"""
    if root == None:
        return
    node = root
    tem = []
    queue = []
    while queue or node:
        while node:
            tem.append(node.val)
            queue.append(node)
            node = node.right
        node = queue.pop()
        node = node.left
    print(tem[::-1])

