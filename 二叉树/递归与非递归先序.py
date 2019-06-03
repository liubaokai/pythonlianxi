"""递归"""
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

"""非递归"""
# 先序打印二叉树（非递归）
# def preOrderTravese(node):
#     stack = [node]
#     while len(stack) > 0:
#         print(node.val)
#         if node.right is not None:
#             stack.append(node.right)
#         if node.left is not None:
#             stack.append(node.left)
#         node = stack.pop()
"""对栈的理解出现问题"""
"""
建立空栈对应于创建一个空白【】，判空栈对应于检查是都为空表
压入元素应在表的尾端进行，对应于list.append
访问栈顶元素应该用list【-1】
弹出操作也应该在表尾端进行，无参的list.pop（）默认弹出表尾元素
"""


def pre_order_stack(root):  # 堆栈实现前序遍历（非递归）
    if not root:
        return
    myStack = []
    node = root
    while myStack or node:
        while node:  # 从根节点开始，一直寻找他的左子树
            print(node.data)
            myStack.append(node)
            node = node.left
        node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = node.right  # 开始查看它的右子树




# 后序打印二叉树（非递归）
# 使用两个栈结构
# 第一个栈进栈顺序：左节点->右节点->跟节点
# 第一个栈弹出顺序： 跟节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
# 第二个栈存储为第一个栈的每个弹出依次进栈
# 最后第二个栈依次出栈
# def postOrderTraverse(node):
#     stack = [node]
#     stack2 = []
#     while len(stack) > 0:
#         node = stack.pop()
#         stack2.append(node)
#         if node.left is not None:
#             stack.append(node.left)
#         if node.right is not None:
#             stack.append(node.right)
#     while len(stack2) > 0:
#         print(stack2.pop().val)
#没问题  举个例子能走通

# 后续遍历根结点，先遍历左子树，然后遍历右子树，此时反过来考虑：先遍历根结点，然后遍历右子树，最后是左子树，这样就
# 可以转化为和先序遍历一个类型了，最后只把遍历结果逆序输出就ok了，而先序遍历是之前写过并且比较好理解的。
#
# 使用栈存储结点；
# 当结点存在或者栈不为空，判断结点；
# 当结点存在，结点值保存，结点入栈，并将指针指向结点的右子树；
# 当栈不为空，结点出栈，并将指针指向左子树；
# 重复2 - 4
# 直到结果产生；
# 逆序输出结果，利用Python列表的 - 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 就用过这个方法了
def postorderTraversal(root):
    ret = []
    stack = []
    while root or stack:
        while root:
            ret.append(root.val)
            stack.append(root)
            root = root.right
        if stack:
            top = stack.pop()
            root = top.left
    return ret[::-1]
def pre_order_stack(root):  # 堆栈实现前序遍历（非递归）
    if not root:
        return
    myStack = []
    node = root
    while myStack or node:
        while node:  # 从根节点开始，一直寻找他的左子树
            print(node.data)
            myStack.append(node)
            node = node.left
        node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = node.right